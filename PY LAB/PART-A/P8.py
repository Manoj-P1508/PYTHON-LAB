import pandas as pd

data=pd.Series([45,78,62,90,55,81,73],index=['asha','usha','sneha','meena','mani','ravi','kiran'])
print("Pandas Series:\n",data)

#indexing
print("\nMarks of mani:",data['mani'])

#slicing
print("\nMarks from sneha to kiran:\n",data['sneha':'kiran'])

#slicing aceessing by position
print("\nFirst 4 entries:\n",data[0:1])

#querying values greater than 70
print("\nStudent scoring above 70:\n",data[data>70])