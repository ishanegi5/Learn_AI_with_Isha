#Local variable

# def h():
#     a=5
#     print(a)

# h()
# print(a) 











#Enclosing variable

# L->E

# def outer():
#     b=4
#     def inner():
#         print(b)
#     inner()

# outer()














#global variable


# count=5
# def f():
#     print(count)

# f() # ->function call



#type-2
# count=6
# def f():
#     global count
#     count=3
#     print("inside function: ",count)
# print("before: ",count)
# f()
# print("after : ",count)










#built-in variable

l=[12,24,53,40,15]
print("len: ",len(l))
print("max: ",max(l))
print("min: ",min(l))



