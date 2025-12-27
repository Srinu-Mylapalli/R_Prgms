def greet(name, greeting="Hello"):
    """Prints a greeting message."""
    print(f"{greeting}, {name}!")

# Using default greeting
greet("Alice")           # Output: Hello, Alice!

# Providing a custom greeting
greet("Bob", "Hi")       # Output: Hi, Bob!

# Providing both parameters explicitly
greet(name="Eve", greeting="Good morning")  # Output: Good morning, Eve!

