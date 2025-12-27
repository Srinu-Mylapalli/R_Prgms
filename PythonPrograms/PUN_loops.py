n = int(input("Enter the value of n: "))

for num in range(2, n + 1):
    is_prime = True  # Assume num is prime
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False  # num is divisible by i, so not prime
            break
    if is_prime:
        print(num, end=' ')

