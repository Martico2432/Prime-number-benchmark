import time
import math
import os
from tqdm import tqdm

def clear_screen():
    # Clear screen command based on OS
    os.system('cls' if os.name == 'nt' else 'clear')

def sieve_of_eratosthenes(num_primes):
    limit = 1000000  # Start with a reasonable limit
    primes = 2
    largest_prime = 2
    is_prime = [True] * (limit + 1)
    p = 2
    
    clear_screen()  # Clear the screen before starting
    
    with tqdm(total=num_primes) as pbar:
        while primes < num_primes:
            if p * p > limit:
                # Expand the sieve if needed
                new_limit = min(limit * 2, int(math.sqrt(limit) + 1) ** 2)
                is_prime += [True] * (new_limit - limit)
                limit = new_limit
            if is_prime[p]:
                primes = p
                pbar.update(1)  # Update progress bar
                if p > largest_prime:
                    largest_prime = p
                for i in range(p * p, limit + 1, p):
                    is_prime[i] = False
            p += 1
    
    return largest_prime

if __name__ == "__main__":
    total_primes = 100000
    print(f"Benchmark started with {total_primes}")
    start_time = time.time()
    largest_prime = sieve_of_eratosthenes(total_primes)
    end_time = time.time()
    total_time = end_time - start_time
    # Multiply total_time by 10 for benchmark-like punctuation
    punctuation = total_time * 10

    print(f"Total time taken: {total_time:.6f} seconds")
    print(f"Largest prime number found: {largest_prime}")
    print(f"Punctuation: {punctuation:.6f}")
