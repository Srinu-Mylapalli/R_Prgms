def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def generate_primes(limit):
    """Generate a list of primes up to the given limit."""
    primes = []
    for number in range(2, limit + 1):
        if is_prime(number):
            primes.append(number)
    return primes

def main():
    n = int(input("Enter the value of n: "))
    primes = generate_primes(n)
    print(f"Prime numbers up to {n}:")
    print(primes)
    nop=0
    for p in primes:
        nop+=1
    fp=open("primesList.txt",'w')
    fp.write(str(primes))

    fp.close()

    print("nop:",nop)
if __name__ == "__main__":
    main()

