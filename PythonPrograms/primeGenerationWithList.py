def generate_primes(n):
    """
    Generate a list of prime numbers up to n.

    Parameters:
    n (int): The upper limit to generate primes.

    Returns:
    list: A list of prime numbers less than or equal to n.
    """
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Example usage
n = int(input("Enter a number: "))
prime_list = generate_primes(n)
print(f"Prime numbers up to {n}:", prime_list)

