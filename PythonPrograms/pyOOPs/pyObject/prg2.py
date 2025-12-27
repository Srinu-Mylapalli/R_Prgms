class Dog:
    species="Canine" #class attribute
    def __init__(self,name,age):
        self.name=name #instance attribute
        self.age=age #instance attribute

dog1=Dog("Buddy",3)
dog2=Dog("Charlie",5)

print(dog1.name,dog1.age,dog1.species) # Access instance and class attributes
print(dog2.name,dog2.age,dog2.species) # Access instance and class attributes
print(Dog.species) # Access class attributes directly
