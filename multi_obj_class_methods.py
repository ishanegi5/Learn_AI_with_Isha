"""
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
"""
#class methods
class University:
    department="technology"
    def __init__(self,emp_name,age):
        self.name=emp_name
        self.age=age
    @classmethod
    def change_dept(cls,new):
        cls.department=new

    def display(self):        
        return "My name is: {1} and age is: {2} and department is: {0}".format(self.department,self.name,self.age)
    
u1=University("Isha",22)
u2=University("tanu",25)

print()
print(u1.department)
print(u1.display())
u2.change_dept("management")
print(u2.display())
print()
print(u1.display())
print(u1.department)