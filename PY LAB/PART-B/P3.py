def create_employee(emp):
    eid = input("ID: ")
    if eid in emp:
        print("ID exists.")
    else:
        name = input("Name: ")
        dept = input("Dept: ")
        emp[eid] = {'name': name, 'department': dept}
def read_employee(emp):
    eid = input("Enter Employee ID: ")
    employee = emp.get(eid)
    if employee:
        print(f"Employee Details: {employee}")
    else:
        print("Not found.")
def update_employee(emp):
    eid = input("Enter Employee ID: ")
    if eid in emp:
        new_dept = input("New Dept: ")
        emp[eid]['department'] = new_dept
    else:
        print("Not found.")
def delete_employee(emp):
    eid = input("Enter Employee ID: ")
    if eid in emp:
        del emp[eid]
        print(f"Employee {eid} deleted.")
    else:
        print("Not found.")
emp = {}
while True:
    print("1.Create 2.Read 3.Update 4.Delete 5.Exit")
    ch = input("Choice: ")

    if ch == '1':
        n = int(input("How many employees? "))
        for _ in range(n):
            create_employee(emp)
    elif ch == '2':
        read_employee(emp)
    elif ch == '3':
        update_employee(emp)
    elif ch == '4':
        delete_employee(emp)
    elif ch == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice.")

print("Final Data:", emp)