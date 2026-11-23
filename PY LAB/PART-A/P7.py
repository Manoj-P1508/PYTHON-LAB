import numpy as np

arr1=np.array([10,20,30,40,50,60])
arr2=np.array([1,2,3,4,5,6])

print("Array 1:",arr1)
print("Array 2:",arr2)

sum_arr=arr1+arr2
diff_arr=arr1-arr2
prod_arr=arr1*arr2
div_arr=arr1/arr2

print("\nElement-wise Addition:",sum_arr)
print("\nElement-wise Subtraction:",diff_arr)
print("\nElement-wise Multiplication:",prod_arr)
print("\nElement-wise Division:",div_arr)

reshaped_arr=arr1.reshape(2,3)
print("\nReshaped array (2*3):\n",reshaped_arr)