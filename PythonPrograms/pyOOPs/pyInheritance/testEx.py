class Earth:
    def __init__(self,name):
        self.name=name

    def introduce(self):
        print(f"Hello!,My name is {self.name} and I belong to Earth")


# Single Inheritance
class Asian(Earth):
    def introduce1(self):
        print(f"Hi,My name is {self.name} and I am from Asia")


# Multilevel Inheritance
class Indian(Asian):
    def introduce2(self):
        print(f"Namaste, My name is {self.name} and I am from India.")




class Engineer:
    def introduce3(self):
        print(f"My name is {self.name} and I am an Engineer")

# Multiple Inheritance
class Machine_Learning_Engineer(Earth,Engineer):
    def introduce4(self):
        print(f"My name is {self.name} and I am a  ML Engineer and I train and Maintain AgriTech Robots")


# Hierarchical Inheritance
class American(Earth):
    def introduce5(self):
        print(f"My name is {self.name} and I am from America")




print("p1")
p1=Earth("python")
p1.introduce()

print("p2")

p2=Asian("Java")
p2.introduce()
p2.introduce1()

print("p3")

p3=Indian("C")
p3.introduce()
p3.introduce1()
p3.introduce2()

print("p4")

p4=Machine_Learning_Engineer("Assembly")
#p4.introduce()
p4.introduce3()
p4.introduce4()


print("p5")

p5=American("COBOL")
p5.introduce()
p5.introduce5()

