class Dog:
    # class variables
    species='Canine'
    def __init__(self,name,age):
        # instance variables
        self.name=name
        self.age=age

# create objects
dog1=Dog("Buddy",3)
dog2=Dog("Charlie",5)


# Access class and instance variables
print(dog1.species) #(Class variable)
print(dog1.name) # (Instance variable)
print(dog2.name) # (Instance variable)


# Modify class and instance variables
dog1.name="Max"
print(dog1.name) # (Updated instance variable)

# Modify class variable

Dog.species="Feline"
print(dog1.species) # (Updated class variables)
print(dog2.species)
