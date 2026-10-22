students = []
print("===========STUDENT MANAGEMENT SYSTEM===========")
while True:
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. View Students")
    print("5. Search Student")
    print("6. Exit")
    
    choice = input("Enter Choice (1-6): ")
    if choice == "6":
        print("System Closed !")
        break
    
    if choice == "1":
        print("======Enter Student Details======")
        student_name = input("Enter Name: ")
        student_roll_no = int(input("Enter Roll no: "))
        student_contact = int(input("Enter contact: "))
        student_course = input("Enter Course: ")
        
        item_detail = {"Name":student_name,
                   "Roll_No":student_roll_no,
                   "Contact":student_contact,
                   "Course":student_course }
        
        students.append(item_detail)
        
        print("Student add successfully.")
        
    elif choice == "2":
        roll = int(input("Enter Roll No: "))
        
        for student in students:
            if student["Roll_No"] == roll:
                students.remove(student)
                print("Student Deleted")
                break
            
   # elif choice == "3":
            
    
    elif choice == "4":
        for student in students:
            print(student)
            
    elif choice == "5":
        roll = int(input("Enter Roll No: "))
        found = False
        
        for student in students:
            if student["Roll_No"] == roll:
                print(student)
                found = True
                
        if not found:
            print("Student Not Found")
            
    else:
        print("Invalid Choice!")
        
        