students={
    101:{"Name":"Asha","Age":18,"Course":"BCA"},
    102:{"Name":"Usha","Age":19,"Course":"BSc"},
    103:{"Name":"Meesha","Age":18,"Course":"Bcom"},
    104:{"Name":"Meena","Age":20,"Course":"BA"},
}

roll_no=int(input("Enter student roll number:"))

if roll_no in students:
    print("Student Details:")
    print("Name:",students[roll_no]["Name"])
    print("Age:",students[roll_no]["Age"])
    print("Course:",students[roll_no]["Course"])
else:
    print("No students foud with Roll number",roll_no)