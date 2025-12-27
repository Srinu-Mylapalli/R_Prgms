def sqrt(number, tolerance=1e-10):
    if number < 0:
        return None  # Square root of negative number is not real

    guess = number / 2.0  # Initial guess
    while True:
        next_guess = (guess + number / guess) / 2
        if abs(next_guess - guess) < tolerance:
            return next_guess
        guess = next_guess

# Example usage:
num = float(input("Enter a number to find the square root: "))
result = sqrt(num)
if result is None:
    print("Square root of negative numbers is not supported.")
else:
    print(f"Square root of {num} is approximately {result}")

