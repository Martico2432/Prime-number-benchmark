import time
import math
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

def clear_screen():
    # Clear screen command based on OS
    os.system('cls' if os.name == 'nt' else 'clear')

def sieve_of_eratosthenes(start, end):
    limit = end  # Start with a reasonable limit
    primes = []
    is_prime = [True] * (limit + 1)
    p = 2
    
    for p in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
    
    for p in range(start, end + 1):
        if is_prime[p]:
            primes.append(p)
    
    return primes

def find_largest_prime(num_primes, num_threads=10):
    limit = 1000000  # Initial sieve limit
    largest_prime = 2
    primes_found = 0
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        chunk_size = num_primes // num_threads
        
        for i in range(num_threads):
            start = i * chunk_size + 2
            end = start + chunk_size - 1 if i < num_threads - 1 else num_primes
            futures.append(executor.submit(sieve_of_eratosthenes, start, end))
        
        clear_screen()  # Clear the screen before starting
        
        with tqdm(total=num_primes) as pbar:
            for future in as_completed(futures):
                primes = future.result()
                primes_found += len(primes)
                pbar.update(len(primes))
                if primes:
                    largest_prime = max(largest_prime, max(primes))
    
    return largest_prime

if __name__ == "__main__":
    total_primes = 100000
    print(f"Benchmark started with {total_primes} primes")
    start_time = time.time()
    largest_prime = find_largest_prime(total_primes)
    end_time = time.time()
    total_time = end_time - start_time
    punctuation = total_time * 10

    print(f"Total time taken: {total_time:.6f} seconds")
    print(f"Largest prime number found: {largest_prime}")
    print(f"Punctuation: {punctuation:.6f}")
