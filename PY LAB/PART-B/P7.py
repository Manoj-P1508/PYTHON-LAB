import matplotlib.pyplot as plt

students=["ram","ramu","raju","radha","ravi"]
marks=[85,78,92,88,76]

#line graph
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.plot(students,marks,marker='o',color='blue',linestyle='-')
plt.title("students marks - line graph")
plt.xlabel("students")
plt.ylabel("marks")
plt.grid(True)

plt.subplot(1,2,2)
plt.bar(students,marks,color='green')
plt.title("student marks - bar chart")
plt.xlabel("students")
plt.ylabel("marks")

plt.tight_layout()
plt.show()