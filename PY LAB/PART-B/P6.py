with open("student_marks.txt","w") as file:
    num_students=int(input("Enter number of students:"))
    for _ in range(num_students):
        name=input("Enter student name: ")
        marks=input("Enter marks: ")
        file.write(f"{name} - {marks}\n")

print("\nData written to 'student_marks.txt' successfully")

print("Contents of 'student_marks.txt':")
with open("student_marks.txt","r") as file:
    contents=file.read()
    print(contents)