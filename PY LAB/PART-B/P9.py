import pandas as pd
data={
    "Product":["Apple","Banana","Apple","Banana","Orange","Orange","Apple","Banana"],
    "Price":[50,30,55,35,60,65,52,32],
    "Quantity":[10,20,15,25,12,18,14,22]
}
df=pd.DataFrame(data)
print("Original DataSet:\n",df,"\n")

grouped=df.groupby("Product").agg({
    "Price":["mean","min","mean"],
    "Quantity":["sum","mean"]
})
print("Grouped Summary Statistics:\n",grouped)