import json
import re
class Student:
    def add_student(self):
        while(True):
            print("Please give details of student:")
            self.name = input("Name: ")
            self.id=input("Id:")
            nodata=0
            found=0
            with open("data_files/students.json","r") as f:
                try:
                    data = json.load(f)
                    if not data:
                        raise error
                except:
                    nodata=1

                if nodata==0:
                    for i in data:
                        if i["id"] == self.id:
                            print("Student with this id already exists.Id must be unique")
                            found=1
                            break
                
            if found==1:
                continue
            else:
                break

       
        self.address = input("Address: ")
        while True:
            self.email = input("Email: ")
            if re.match(r"^[a-zA-Z0-9._%+-]+@gmail\.com$", self.email):
                break
            else:
                print("Invalid email format. Please try again.")
        while True:
            self.phone_number = input("Phone number: ")
            if re.match(r"^\d{10}$", self.phone_number):
                self.phone_number = int(self.phone_number)
                break
            else:
                print("Phone number must be exactly 10 digits. Please try again.")
        print("Give marks of student:")
        mark=[]
        for i in range(3):
            mark.append(float(input("Mark[" + str(i+1) + "]:")))
        self.marks=mark
        with open('data_files/students.json',"r+",newline="\n") as f:
            try:
                data = json.load(f) 
            except:
                data=[]
                
            f.seek(0)  #so that we can erase file from beginning
            f.truncate() #so that we can erase file from beginning
            data.append(self.__dict__) #self.dict gives all attributes of this object in dictionary
            json.dump(data, f, indent=4)
            print("student added successfully")
                    

    def search_student(self):
        print("Enter student id to search: ")
        id=input("Id:")
        with open('data_files/students.json',"r") as f:
            try:
                data = json.load(f) 
            except:
                print("No data in the database")
                return
        
        for i in data:
            if i["id"] == id:
                print("Student found: ")
                print("Name: ",i["name"])
                
                print("Address: ",i["address"])
                print("Email: ",i["email"])
                print("Phone number: ",i["phone_number"])
                print("Marks: ",i["marks"])
                return
        print("Student id not found")

    def update_student(self):
        print("Enter student id to update: ")
        id=input("Id:")
        with open('data_files/students.json',"r+",newline="\n") as f:
            try:
                data = json.load(f) 
            except:
                print("No data in the database")
            found=0

            for i in data:   
                if i["id"] == id:
                    found=1
                    print("Student found, enter new details: ")
                    i['name'] = input("Name: ")
                    i['address'] = input("Address: ")
                    while True:
                        self.email = input("Email: ")
                        if re.match(r"^[a-zA-Z0-9._%+-]+@gmail\.com$", self.email):
                            break
                        else:
                            print("Invalid email format. Please try again.")
                    while True:
                        self.phone_number = input("Phone number: ")
                        if re.match(r"^\d{10}$", self.phone_number):
                            self.phone_number = int(self.phone_number)
                            break
                        else:
                            print("Phone number must be exactly 10 digits. Please try again.")
                    print("Give marks of student:")
                    mark=[]
                    for j in range(3):
                        mark.append(float(input("Mark[" + str(j+1) + "]:")))
                    i['marks']=mark
                    break
            if found==0:
                print("Student not found")
                return
            f.seek(0)  #so that we can erase file from beginning
            f.truncate()
            json.dump(data, f, indent=4)
            print("Student updated successfully")
        

    def delete_student(self):
        print("Enter student id to delete: ")
        id=input("Id:")
        with open('data_files/students.json',"r+",newline="\n") as f:
            try:
                data = json.load(f) 
                if not data:
                    raise error
                
            except:
                print("No data in the database")
                return 
            found=0
            for i in data:   
                if i["id"] == id:
                    found=1
                    data.remove(i)
                    break
            if found==0:
                print("student not found")
                return
            f.seek(0)  #so that we can erase file from beginning
            f.truncate()
            json.dump(data, f, indent=4)
            print("student deleted successfully")


    def show_all_students(self):
        
        with open('data_files/students.json',"r") as f:
            try:
                data = json.load(f) 
                if not data:
                    raise error
            except:
                print("No data in the database")
                return 
        
        for i in data:
            print(i)



    def pass_fail_determination(self,id):
        
        with open('data_files/students.json',"r") as f:
            try:    
                data = json.load(f)
                if not data:
                    raise error
            except:
                print("No data in the database")
                return
            found=0
            for i in data:   
                if i["id"] == id:
                    found=1
                    if i["marks"][0]>=40 and i["marks"][1]>=40 and i["marks"][2]>=40:
                        print("PASS")
                    else:
                        print("FAIL")
                    break
            if found==0:
                print("student not found")
                return
        

    def high_marks(self,id):
        with open('data_files/students.json',"r") as f:
            try:
                data = json.load(f)
                if not data:
                    raise error
            except:
                print("No data in the database")
                return
            found=0
            for i in data:   
                if i["id"]==id:
                    found=1
                    print("Highest marks: ",max(i["marks"]))
                    break
            if found==0:
                print("student not found")
                return
            

    def low_marks(self,id):
        with open('data_files/students.json',"r") as f:  
            try:
                data = json.load(f)
                if not data:
                    raise error
            except:
                print("No data in the database")
                return
            found=0
            for i in data:   
                if i["id"] == id:
                    found=1
                    print("Lowest marks: ",min(i["marks"]))
                    break
            if found==0:
                print("student not found")
                return  
            
    def percentage(self,id):
        with open('data_files/students.json',"r") as f:
            try:
                data = json.load(f)
                if not data:
                    raise error
            except:
                print("No data in the database")
                return
            found=0
            for i in data:   
                if i["id"] == id:
                    found=1
                    print("Percentage: ",sum(i["marks"])/3)
                    break
            if found==0:
                print("student not found")
                return
            

    def rank_calculation(self,id):
        with open('data_files/students.json',"r") as f:
            try:
                data = json.load(f)
                if not data:
                    raise error
            except:
                print("No data in the database")
                return
            found=0
            for i in data:   
                if i["id"] == id:
                    found=1
                    percentage=sum(i["marks"])/3
                    break
            if found==1:
                rank=len(data)
                
                for i in data:
                    if i["id"] != id:
                        percent=sum(i["marks"])/3
                        if percentage>=percent:
                            rank=rank-1
                print("Rank: ",rank)
                return 
            if found==0:
                print("student not found")
                return
            
    
                


    
            
        
# s=Student()
# s.add_student()
# s.search_student()
# s.update_student()
# s.delete_student()
# s.show_all_students()
# s.low_marks("a")
# s.high_marks("a")
# s.percentage("a")