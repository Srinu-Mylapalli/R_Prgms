# Hill Climbing Algorithm in Python

import random

# Function we want to maximize
def f(x):
    return -(x - 10)**2 + 100   # Peak at x = 10

def hill_climbing():
    # Start with a random solution
    current = random.randint(1, 20)
    print("Starting at:", current)

    while True:
        # Generate two neighbors
        neighbors = [current - 1, current + 1]

        # Select the neighbor with the highest value of f(x)
        next_node = max(neighbors, key=f)

        # If the neighbor is not better, stop
        if f(next_node) <= f(current):
            print("Reached peak.")
            return current, f(current)

        # Move to the better neighbor
        current = next_node
        print("Moving to:", current)

# Run the algorithm
best_x, best_value = hill_climbing()
print("Best solution:", best_x)
print("Best value:", best_value)
