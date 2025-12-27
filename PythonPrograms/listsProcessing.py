import random
import itertools

# Original list
numbers = [4, 2, 9, 1, 7, 3]
words = ['banana', 'apple', 'grape', 'cherry']

# 1. Sorting a list
sorted_numbers = sorted(numbers)
sorted_words = sorted(words)
print("Sorted numbers:", sorted_numbers)
print("Sorted words:", sorted_words)

# 2. Flexible sorting (e.g., by length or reverse)
sorted_by_length = sorted(words, key=len)
sorted_desc = sorted(numbers, reverse=True)
print("Words sorted by length:", sorted_by_length)
print("Numbers sorted descending:", sorted_desc)

# 3. Searching in a list
if 7 in numbers:
    print("7 is in the list at index:", numbers.index(7))
else:
    print("7 is not in the list.")

# 4. Generating all permutations of a list
perms = list(itertools.permutations([1, 2, 3]))
print("Permutations of [1, 2, 3]:", perms)

# 5. Randomly permuting (shuffling) a list
shuffled = numbers[:]  # make a copy
random.shuffle(shuffled)
print("Shuffled numbers:", shuffled)

# 6. Reversing a list
reversed_list = list(reversed(numbers))
print("Original numbers:", numbers)
print("Reversed numbers:", reversed_list)

