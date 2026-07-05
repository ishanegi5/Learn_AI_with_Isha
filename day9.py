"""
#functions
def greet():
    print("Hello, ML world")

greet() #func call




def vari():
    a=2
    print("hello ",a)
    return a

print(vari())



def add(a,b): #a,b=> parameters
    c=a+b
    return c

print(add(5,7)) #a,b=>argument



def square(num=3):
    return num*num

print(square(7))
"""

def add(a,b): #a,b=> parameters
    print(b,a)
    c=a+b
    return c

print(add(b=5,a=7))