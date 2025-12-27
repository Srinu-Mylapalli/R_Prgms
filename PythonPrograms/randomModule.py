import random as rd
print(rd.random()) # Displays a value between 0 and 1
print(rd.randint(5,10)) # Displays a random integer from the given range
print(rd.randrange(1,10,2)) # Displays a number from 3,5,7,9

lis=["A","B","C","D","E"]
print(rd.choice(lis)) # returns a random value from the sequence
