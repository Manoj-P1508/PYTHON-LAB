def show(lst):
    if not lst:
        print("Current list is empty.")
    else:
        print("Current list:")
        for index,value in enumerate(lst):
            print(f"{index}:{value}")

def insert_element(lst):
    value=input("Enter value to insert:")
    lst.append(value)
    show(lst)
    
def delete_by_value(lst):
    value=input("Enter value to delete: ")
    if value in lst:
        lst.remove(value)
    else:
        print("Value not found")
    show(lst)
    
def delete_by_index(lst):
    try:
        idx=int(input("Enter index to delete: "))
        lst.pop(idx)
    except(ValueError,IndexError):
        print("Invaild index")
    show(lst)

def update_element(lst):
    try:
        idx=int(input("Enter index to delete: "))
        new_val=input("Enter new value: ")
        lst[idx]=new_val
    except(ValueError,IndexError):
        print("Invaild index")
    show(lst)
    
items=[]
while True:
    print("\nMenu")
    print("1. Insert element")
    print("2. Delete by value")
    print("3. Delete by index")
    print("4. Update element at index")
    print("5. Show list")
    print("6. Exit")
    
    choice=input("Enter choice: ").strip()
    
    if choice=="1":
        insert_element(items)
    elif choice=="2":
        delete_by_value(items)
    elif choice=="3":
        delete_by_index(items)
    elif choice=="4":
        update_element(items)
    elif choice=="5":
        show(items)
    elif choice=="6":
        print("Program ended.")
        break
    else:
        print("Invalid choice.")