class PrimeSieve:
    def __init__(self, limit):
        self.limit = limit
        self.prime_flags = [True] * (limit + 1)
        self.prime_flags[0], self.prime_flags[1] = False, False

    def _sieve(self):
        for current in range(2, int(self.limit ** 0.5) + 1):
            if self.prime_flags[current]:
                for multiple in range(current * current, self.limit + 1, current):
                    self.prime_flags[multiple] = False

    def get_primes(self):
        self._sieve()
        return [num for num, is_prime in enumerate(self.prime_flags) if is_prime]


# Example usage:
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    sieve = PrimeSieve(n)
    primes = sieve.get_primes()
    print(f"Prime numbers up to {n}:")
    print(primes)

