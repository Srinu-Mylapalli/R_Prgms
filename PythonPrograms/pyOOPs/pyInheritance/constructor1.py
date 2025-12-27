# parameterized construct

class Student:
    #self.rollno=rollno
    #self.name=name
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
        print(self.rollno)
        print(self.name)

std=Student(12,"CSE")
s1=Student(13,"AIML")
