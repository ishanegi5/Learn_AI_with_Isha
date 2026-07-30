
#static method-> independent from the varibales (instance or class)
class Calculator:
    @staticmethod
    def add(a,b):
        return a+b
    

c=Calculator()
print(c.add(2,18))

#no need of self
#no need of cls
#used using @staticmethod decorator only 
"""
   if static method decorator is not used it would expect a starting 
   parameter(self,cls) for passing object or class 
   But if you use @staticmethod decorator then no need to use self  or cls 
   only give your arguments to be calculated that's it.
"""