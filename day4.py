#list
# l=[12,52,38,50] 
# s={12,52,38,50}
# print(s)
# print(l)

#mutable
# l=[45,67,89]
# print("before: ",l)
# l[0]=3
# print("after: ",l)

# l=[3,7,8]
# l=["isha",3,5.7,True]
# print(l)
# print(type(l))

# print(l[2]) 

# l.append("tanu")
# print(l)

# l.remove("isha")
# print(l) 

# print(l[5])






#tuple
# t=(15,78,5)
# print(type(t))
# #t[0]=4

# t1=("isha",4,8.5,True)
# print(type(t1))

# print(t1[2])









#dictionary
#d={"name":"isha",1:7,"marks":67,True:1,4.5:"yes"}
d={"name":"isha","y":6,1:7}
# print(d.keys()) #-> for printing keys in dictionary
# print(d.values()) #-> for printing values in dictionary
# print(d["name"]) #-> for printing value of a key in dictionary
# print(d[1]) #-> for printing element at a particular index in a dictionary
# print(d.index(0)) #checking if we can access key-value pairs in a dictionary using index(0,1,2,...)
# print(d["marks"]) #checking if its possible to get a value for a key that's not present
# print(d.get("marks","not a key"))  #using get function to avoid error (code phatna) using a statement
# print(d.get("marks"))  #using get function to avoid error (code phatna) without using a statement

d["marks"]=95 #adding an element in dictionary
d["name"]="tanu" #updating a dictionry value 

#we cannot update a key we can only update a value out of the key-value pairs in a dictionary
print(d) #printing dictionary
del d["marks"] #deleting a key from dictionary
print(d)
del d #deleting full dictionary 
print(d) #NameError 