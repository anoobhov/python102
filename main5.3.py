#
def print_choice_message():
    print("Select your choice")
    print("1.Add a record")
    print("2.Update a record")
    print("3.Get a record")
    print("4.Exit")

def get_student_details():
    print("Enter student name: ", end=" ")
    name=input()
    print("Enter students marks: ", end=" ")
    marks=int(input())

    return name,marks


record=dict()
print("---Welcome to the class---")
while True:
    print_choice_message()

    choice=int(input())
    if choice == 1 or choice == 2:
        name,marks=get_student_details()
        record[name]=marks
    elif choice == 3:
        print("Enter student name: ",end=" ")
        name=input()
        print("The marks is ",record[name])
    else:
        break

