"""
#loops
fruits=["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)







#loop through string
for letter in "ML":
    print(letter)





#range function use->mostly used
for i in range(7):
    print(i)

"""
"""first example of while loop similar to for loop and it also shows the difference 
 1)variable needs to be initialized earlier 
 2)explicit need of increment the initialized variable unlike for loop case


j=0
while(j<7):
    print(j)
    j+=1


#2nd example - infinite while loop - using boolean
while True:
    print("sn")





#3rd example - infinite while loop
s=2
while s<5:
    print("sn")



#understanding range function (start,stop,step)-> range(2,7,3) ->2,5
for i in range(2,7,3):
    print(i)


#single value
for i in range(5):
    print(i)  #0,1,2,3,4


for i in range(5,12):
    print(i)  #5,6,7,8,9,10,11


#reverse use of range:
for i in range(10,0,-2): #note upper bound is excluded and lower bound is included 
    print(i)

for i in range(10,2,2): #what will be the output of this? be careful!
    print(i)
    
"""
"""
NOTE:if going upward (positive step),start must be less than Stop
and vice versa for downward(negative step).

for i in range(10,2):
    print(i)
"""
"""
Note range function is generally used for ->for loop


#bonus
for i in range(5):
    print(i,end="") #->01234
"""
"""
#break and continue
for i in range(5):
    if(i==3):
        break
    print(i)
"""

for i in range(7):
    if(i==4):
        continue
    print(i)
