class Parent:
    def display(self):
        print("Parent class")

class Child(Parent):
    def display1(self):
        print("Child class")

c=Child()

c.display()
c.display1()

