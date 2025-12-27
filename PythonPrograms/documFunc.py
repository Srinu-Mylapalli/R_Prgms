def greet(name):
    """
    Greet the person by name.

    Parameters:
    name (str): The name of the person.

    Returns:
    None
    """
    print(f"Hello, {name}!")

# Method 1: Using the __doc__ attribute
print(greet.__doc__)

# Method 2: Using the help() function
#help(greet)

