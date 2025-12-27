class World:
    def __init__(self,name):
        self.name=name

    def introduction(self):
        print(f"Hello !, My name is {self.name} I am a world citizen")

class Asian(World):
    def introduction_1(self):
        print("I am an Asian")

'''class Indian(World,Asian):
    def introduction_2(self):
        print("I am an Indian")'''

'''class AndhraPradesh(Indian):
    def introduction_3(self):
        print("I am from AndhraPradesh")
'''
class American(World):
    def introduction_4(self):
        print("I am from America")



p1=World("Python")
p2=Asian()
p3=Indian()
p4=AndhraPradesh()
p5=American()


p1.introduction()
p2.introduction_1()
p2.introduction()

#p3.introduction_2()
p4.introduction_3()
p5.introduction_4()
