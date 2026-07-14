"""
#4. invalid input from user
try:
    k=int(input("Enter the value of k for KNN: "))
    if(k<=0):
        raise ValueError("K must be a positive integer")
except ValueError as ve:
    print("Invalid input: ",ve)







"""














# 5. handling missing columns
config={"learning_rate":0.01,"batch_size":32}
try:
    epochs=config["epochs"]
except KeyError:
    print("key epochs not found in config using default value: 10")
    epochs=10
