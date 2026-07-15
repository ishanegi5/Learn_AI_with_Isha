#class
class Student:

    #attribute
    school="ABC school"

    #constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("constructor")
        print(self)
    
    #method
    def greet(self):
        print("hi ",self.name,"\nmy age is: ",self.age)

#object
# s1=Student()  #without constructor object making
s1=Student("isha",25)
# print(s1.school) #attribute
s1.greet()  #method