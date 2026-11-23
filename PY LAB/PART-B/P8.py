import pandas as pd

csv_data="""Rollno,Name,Marks,Course
1,raj,85,BCA
2,ram,78,BSc
3,Ravi,92,BCom
4,rakhi,88,BCA
5,rohi,76,BSc
"""
with open("students.csv","w") as file:
    file.write(csv_data)
    
print("CSV file 'students.csv' created successfully.\n")

df=pd.read_csv("students.csv")
print("Data loaded from CSV:\n",df,"\n")
print("First 3 rows of the dataset:\n",df.head(3),"\n")
print("Last 2 rows of the dataset:\n",df.tail(2),"\n")
print("Summary statistics for numeric columns:\n",df.describe(),"\n")
print("Data types of each column:\n",df.dtypes,"\n")
print("Average marks of students:",df["Marks"].mean(),"\n")
print("students with marks greater than 80:\n",df[df["Marks"]>80])