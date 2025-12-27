import random
import itertools
from operator import attrgetter

# Define a Student class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __repr__(self):
        return f"{self.name} ({self.marks})"

# Create a list of Student objects
students = [
    Student("Alice", 85),
    Student("Bob", 92),
    Student("Charlie", 78),
    Student("Diana", 92)
]

# 1. Sorting students by marks (ascending)
sorted_by_marks = sorted(students, key=lambda s: s.marks)
print("Students sorted by marks:")
print(sorted_by_marks)

# 2. Sorting by name (alphabetical)
sorted_by_name = sorted(students, key=attrgetter("name"))
print("\nStudents sorted by name:")
print(sorted_by_name)

# 3. Flexible sorting: by marks descending, then by name
sorted_flex = sorted(students, key=lambda s: (-s.marks, s.name))
print("\nStudents sorted by marks descending, then name:")
print(sorted_flex)

# 4. Searching for a student by name
search_name = "Charlie"
found = next((s for s in students if s.name == search_name), None)
print(f"\nSearch result for '{search_name}': {found if found else 'Not found'}")

# 5. Reversing the student list
reversed_students = list(reversed(students))
print("\nReversed student list:")
print(reversed_students)

# 6. Randomly shuffling students
shuffled_students = students[:]  # Copy
random.shuffle(shuffled_students)
print("\nRandomly shuffled students:")
print(shuffled_students)

# 7. Permutations of the first 3 students
perms = list(itertools.permutations(students[:3]))
print("\nPermutations of first 3 students:")
for p in perms:
    print(p)

