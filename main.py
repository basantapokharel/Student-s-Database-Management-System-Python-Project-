import json
from entities.student import Student
from entities.teacher import Teacher


s=Student()
t=Teacher()

while(True):

    print("Login:")
    print("1. Student\t 2. Teacher")
    ch = int(input("Enter your choice: "))
    print(f"Choice entered: {ch}")

    if ch == 1:
        while(True):
            print("Verify as a Student")
            name=input("Enter you name:")
            id=input("Enter your id:")




            with open("data_files/students.json","r") as f:
                try:
                    data=json.load(f)
                    
                    if not data:
                        raise ValueError
                        
                
                except(ValueError,json.JSONDecodeError) as e:
                    print("No data in the database")
                    continue
            found=0
            for i in data:
                if i["name"] == name and i["id"] == id:
                    found=1
                    print("Login successful")
                    while(True):
                        print("1. Check result \t 2. Highest-mark \t 3. Lowest-mark \t 4. Percentage \t 5. Rank-Calculation \t 6. Exit")
                        ch = int(input("Enter your choice: "))
                        if ch == 1:
                            s.pass_fail_determination(id)
                        elif ch == 2:
                            s.high_marks(id)
                        elif ch == 3:
                            s.low_marks(id)
                        elif ch == 4:
                            s.percentage(id)
                        elif ch == 5:
                            s.rank_calculation(id)
                        elif ch == 6:
                            print("Exiting.........")
                            break

                        else:
                            print("Invalid input")
                    break

            break
            if found==0:
                print("Login failed")
                break

    elif ch == 2:
        while(True):
            print("Verify as a Teacher")
            name=input("Enter you name:")
            id=input("Enter your id:")




            with open("data_files/teachers.json","r") as f:
                try:
                    data=json.load(f)
                    
                    if not data:
                        raise ValueError
                        
                
                except(ValueError,json.JSONDecodeError) as e:
                    print("No data in the database")
                    continue
            found=0
            for i in data:
                if i["name"] == name and i["id"] == id:
                    found=1
                    print("Login successful")
                    while(True):
                        print("1. Add student \t 2. Search Student \t 3. Update student \t 4. Delete student \t 5. Show all students \t 6. Add teacher \t 7. Search teacher \t 8. Update teacher \t 9. Delete teacher \t 10. Show all teachers \t 11. Exit")
                        ch = int(input("Enter your choice: "))
                        if ch == 1:
                            s.add_student()
                        elif ch == 2:
                            s.search_student()
                        elif ch == 3:
                            s.update_student()
                        elif ch == 4:
                            s.delete_student()
                        elif ch == 5:
                            s.show_all_students()
                        elif ch == 6:
                            t.add_teacher()
                        elif ch == 7:
                            t.search_teacher()
                        elif ch == 8:
                            t.update_teacher()
                        elif ch == 9:
                            t.delete_teacher()
                        elif ch == 10:
                            t.show_all_teachers()

                        elif ch == 11:
                            print("Exiting.........")
                            break

                        else:
                            print("Invalid input")
                    break

            break
            if found==0:
                print("Login failed")
                break
    else:
        print("Invalid input")


           

                    


        














































































                        
                        

            
                

