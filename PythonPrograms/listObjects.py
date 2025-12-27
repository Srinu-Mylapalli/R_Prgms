# List basics and operations

# Creating lists
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

# Accessing elements
print("First number:", numbers[0])
print("Last fruit:", fruits[-1])

# Modifying elements
fruits[1] = "blueberry"
print("Modified fruits:", fruits)

# List methods
numbers.append(6)
numbers.insert(2, 99)
numbers.remove(3)
last_item = numbers.pop()
numbers.sort()
numbers.reverse()
print("Modified numbers:", numbers)
print("Index of 99:", numbers.index(99))

# Looping through a list
print("All fruits:")
for fruit in fruits:
    print(fruit)

# List comprehension
squares = [x*x for x in range(1, 6)]
print("Squares:", squares)

# Generating prime numbers using a list
def generate_primes(limit):
    """
    Return a list of prime numbers up to the given limit.
    """
    primes = []
    for num in range(2, limit + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes

prime_list = generate_primes(20)
print("Primes up to 20:", prime_list)

