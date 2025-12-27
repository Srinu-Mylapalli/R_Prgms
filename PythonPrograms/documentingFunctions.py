def is_prime(num):
    """
    Check if a number is prime.

    Parameters:
    num (int): The number to check.

    Returns:
    bool: True if num is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def generate_primes(limit):
    """
    Generate a list of prime numbers up to the given limit.

    Parameters:
    limit (int): The upper bound of the range to check for primes.

    Returns:
    list: A list containing all prime numbers up to limit.
    """
    primes = []
    for number in range(2, limit + 1):
        if is_prime(number):
            primes.append(number)
    return primes

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    primes = generate_primes(n)
    print(f"Prime numbers up to {n}:")
    print(primes)

