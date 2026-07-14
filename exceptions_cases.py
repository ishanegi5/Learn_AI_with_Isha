"""
#1. Missing data files
try:
    with open("data.csv","r") as f:
        data=f.read()
except FileNotFoundError:
    print("Error: the dataset file was not found.")












#2. unexpected data format (eg. non-numeric value in numeric column)
import pandas as pd
df=pd.DataFrame({"age":[12,34,56,23,"seventy-seven"]}) #check for "seventy-seven"->then it throws an error

try:
    df['age']=df["age"].astype(int)
    print("i am running try block")
except Exception as e:
    print("your error is: ",e)
"""

"""Note: ""->empy string,
         "~" or "?"->special character
         NaN value-> np.nan
         "seventy-seven"->written in alphabets
         all these will throw the error
"""











#3. division by zero
try:
    a=2/0
    print(a)
except Exception as e:
    print("error: ",e)
