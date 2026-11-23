import pandas as pd
import numpy as np

data={
    "Name":["Asha","Ravi","Ramu","Sneha","Megha"],
    "Marks":[78,np.nan,62,np.nan,85],
    "Age":[18,19,np.nan,20,np.nan]
}

df=pd.DataFrame(data)
print("Original DataFrame\n",df)

mean_marks=df["Marks"].mean()
df["Marks"]=df["Marks"].fillna(mean_marks)

median_age=df["Age"].median()
df["Age"]=df["Age"].fillna(median_age)

print("\nDataFrame after filling missing values:\n",df)