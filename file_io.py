"""
read-"r"
write-"w"
append-"a"


with open("cake.txt","a") as file:
    file.write("\nit's isha")
"""
with open("cake.txt","r") as f:
    for line in f:
        print(line.strip())