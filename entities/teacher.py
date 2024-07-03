import json
import re
class Teacher:
    def add_teacher(self):
        print("Please give details of teacher:")
        self.name = input("Name: ")
        self.subject = input("Subject: ")
        while(True):
            found=0
            self.id=input("Id:")
            with open('data_files/teachers.json',"r") as f:
                try:
                    data = json.load(f) 
                except:
                    data=[]

            for i in data:
                if i["id"] == self.id:
                    print("Teacher with this id already exists.Id must be unique")
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

        with open('data_files/teachers.json',"r+",newline="\n") as f:
            try:
                data = json.load(f) 
            except:
                data = []
            
            f.seek(0)  #so that we can erase file from beginning
            f.truncate() #so that we can erase file from beginning
            data.append(self.__dict__) #self.dict gives all attributes of this object in dictionary
            json.dump(data, f, indent=4)
            print("Teacher added successfully")
        
        

    def search_teacher(self):
        print("Enter teacher id to search: ")
        id=input("Id:")
        with open('data_files/teachers.json',"r") as f:
            try:
                data = json.load(f) 
            except:
                print("No data in the database")
                return
        
        for i in data:
            if i["id"] == id:
                print("Teacher found: ")
                print("Name: ",i["name"])
                print("Subject: ",i["subject"])
                print("Address: ",i["address"])
                print("Email: ",i["email"])
                print("Phone number: ",i["phone_number"])
                return
        print("Teacher id not found")

    def update_teacher(self):
        print("Enter teacher id to update: ")
        id=input("Id:")
        with open('data_files/teachers.json',"r+",newline="\n") as f:
            try:
                data = json.load(f) 
            except:
                print("No data in the database")
                return
            found=0

            for i in data:   
                if i["id"] == id:
                    found=1
                    print("Teacher found, enter new details: ")
                    i['name'] = input("Name: ")
                    i['subject'] = input("Subject: ")
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
                    break
            if found==0:
                print("Teacher not found")
                return
            f.seek(0)  #so that we can erase file from beginning
            f.truncate()
            json.dump(data, f, indent=4)
            print("Teacher updated successfully")




    def delete_teacher(self):
        print("Enter teacher id to delete: ")
        id=input("Id:")
        with open('data_files/teachers.json',"r+",newline="\n") as f:
            try:
                data = json.load(f) 
            except:
                print("No data in the database")
            found=0
            for i in data:   
                if i["id"] == id:
                    found=1
                    data.remove(i)
                    break
            if found==0:
                print("Teacher not found")
                return
            f.seek(0)  #so that we can erase file from beginning
            f.truncate()
            json.dump(data, f, indent=4)
            print("Teacher deleted successfully")


    def show_all_teachers(self):
        with open('data_files/teachers.json',"r") as f:
            try:
                data = json.load(f) 
            except:
                print("No data in the database")
                return 
        
        for i in data:
            print(i)



# t=Teacher()
# t.add_teacher()
# t.search_teacher()
# t.update_teacher()
# t.delete_teacher()
# t.show_all_teachers()

    
