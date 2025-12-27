def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize all entries as True.
    # A value in prime[i] will finally be False if i is not a prime, True if prime.
    prime = [True] * (n + 1)
    prime[0], prime[1] = False, False  # 0 and 1 are not prime numbers

    p = 2
    while p * p <= n:
        if prime[p]:
            # Mark multiples of p as False
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Collect all prime numbers
    primes = [i for i, is_prime in enumerate(prime) if is_prime]
    return primes

# Example usage:
n = int(input("Enter the value of n: "))
primes = sieve_of_eratosthenes(n)
print(f"Prime numbers up to {n}:")
print(primes)

