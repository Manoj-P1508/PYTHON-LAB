from sklearn import datasets
import pandas as pd

iris=datasets.load_iris()
print("Dataset Name:",iris['DESCR'].split("\n")[0])
print("Number of Samples:",iris.data.shape[0])
print("Number of Features:",iris.data.shape[1])
print("Target Names:",iris.target_names,"\n")

df=pd.DataFrame(data=iris.data,columns=iris.feature_names)
df['target']=iris.target

print("First 5 rows of the datasets:\n",df.head())
print("Last 5 rows of the datasets:\n",df.tail())

print("Dataset Info:")
print(df.info(),"\n")
print("Summary Statistics:\n",df.describe())