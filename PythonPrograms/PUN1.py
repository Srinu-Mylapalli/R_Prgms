def generate_prime_flags(limit):
    """Generate a list of boolean flags indicating primality up to limit."""
    prime_flags = [True] * (limit + 1)
    prime_flags[0], prime_flags[1] = False, False  # 0 and 1 are not prime

    for current in range(2, int(limit ** 0.5) + 1):
        if prime_flags[current]:
            # Mark multiples as not prime
            for multiple in range(current * current, limit + 1, current):
                prime_flags[multiple] = False
    return prime_flags

def get_primes_from_flags(prime_flags):
    """Return a list of prime numbers based on prime flags."""
    return [num for num, is_prime in enumerate(prime_flags) if is_prime]

def sieve_of_eratosthenes(n):
    """Return a list of primes up to n using Sieve of Eratosthenes."""
    flags = generate_prime_flags(n)
    return get_primes_from_flags(flags)

# Example usage:
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    primes = sieve_of_eratosthenes(n)
    print(f"Prime numbers up to {n}:")
    print(primes)

