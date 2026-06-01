
students = {}

while True:
    print("\n--- Student Record System ---")
    print("1. Add Student")
    print("2. View Student")
    print("3. View All Students")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        students[roll_no] = {
            "Name": name,
            "Marks": marks
        }
        print("Student record added successfully!")

    elif choice == 2:
        roll_no = input("Enter Roll Number: ")
        if roll_no in students:
            print("Student Details:")
            print("Name:", students[roll_no]["Name"])
            print("Marks:", students[roll_no]["Marks"])
        else:
            print("Student not found!")

    elif choice == 3:
        if students:
            print("\nAll Student Records:")
            for roll_no, details in students.items():
                print(f"Roll No: {roll_no}, Name: {details['Name']}, Marks: {details['Marks']}")
        else:
            print("No records found!")

    elif choice == 4:
        roll_no = input("Enter Roll Number to delete: ")
        if roll_no in students:
            del students[roll_no]
            print("Record deleted successfully!")
        else:
            print("Student not found!")

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
