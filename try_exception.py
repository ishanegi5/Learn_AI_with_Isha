#try except 
"""
with open("non_existent.txt","r") as f:
    print(f.read())










"""
try:
    with open("non_existent.txt","r") as f:
        print(f.read())
except Exception as e:
    print("Error: ",e)
finally:
    print("This always runs.")
