import pandas as pd

data="""Rollno,Name,Marks,Course
1,Mani,78,BCA
2,Prathap,88,BSc
3,shankar,62,Bcom
4,charan,90,BA
5,Navneeth,55,BCA
6,Yathish,81,Bsc
7,Vikran,92,BA
8,Rohith,73,Bcom
"""

with open("students.csv","w") as file:
    file.write(data)

df=pd.read_csv("students.csv")

print("\nOriginal Dataframe:\n",df)