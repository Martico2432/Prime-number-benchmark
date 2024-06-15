import time
import math
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

def clear_screen():
    # Clear screen command based on OS
    os.system('cls' if os.name == 'nt' else 'clear')

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    primes = []
    
    while len(primes) < limit:
        if p > limit:
            break
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    
    return primes

def find_largest_prime(num_primes, num_threads=10):
    total_primes = num_primes
    limit = 1000000  # Initial sieve limit
    largest_prime = 2
    primes_found = 0
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        chunk_size = limit // num_threads
        
        for i in range(num_threads):
            start = i * chunk_size + 2
            end = start + chunk_size - 1 if i < num_threads - 1 else limit
            futures.append(executor.submit(sieve_of_eratosthenes, end))
        
        clear_screen()  # Clear the screen before starting
        
        with tqdm(total=total_primes, unit='prime') as pbar:
            for future in as_completed(futures):
                primes = future.result()
                primes_found += len(primes)
                if primes_found >= total_primes:
                    break
                for prime in primes:
                    if prime > largest_prime:
                        largest_prime = prime
                        pbar.update(1)
    
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
