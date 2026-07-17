#multiple object
class Employee:
    company="google"
    def __init__(self,emp_name,age):
        self.name=emp_name
        self.age=age
    def display(self):        
        return "My name is: {} and age is: {}".format(self.name,self.age)
    
e1=Employee("Isha",21)
e2=Employee("Tanu",23)
print(e1.name)
print(e1.company)
print(e1.display()) #Employee.display(e1)
print() #\n

print(e2.name)
print(e2.company)
print(e2.display())
#class methods