import json
import os

# ------ Classes ------
class Operation:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    # ---- Update marks ----
    def update(self,marks):
        if marks < 0:
            raise ValueError("Marks need to be positive")
        if marks > 100:
            raise ValueError("Marks need to be under 0-100")
        self.marks = marks
    # ---- Save data in dict ----
    def to_dict(self):
        return {
            "Name" : self.name,
            "Marks" : self.marks
        }

# ------ Main Class ------
class Student:
    File = "Database.json"
    def __init__(self):
        self.students = {}
        self.load()
    
    # ---- To Save ----
    def save(self):
        with open(self.File,"w") as f:
            json.dump(
                {k: v.to_dict() for k,v in self.students.items()} , f, indent = 5
            )

    # ---- To Load ----        
    def load(self):
        data = {}

        # if os path exist
        
        if os.path.exists(self.File):
            try:
                with open(self.File) as f:
                    data = json.load(f)
                
                for k,v in data.items():
                    self.students[k] = Operation(v["Name"], v["Marks"])

            except json.JSONDecodeError:
                self.data = {}
   
    #----- Main Core -----
    def add_student(self,name,marks):

        stud = Operation(name,marks)
        self.students[name] = stud
        self.save()

        print(f"Student {name} is now added")

    def show(self):
        with  open(self.File) as f:
            show_ = json.load(f)
        for key,item in show_.items():
            print(f"{key} : {item}")

    def update_mark(self,name,new_marks):

        if name in self.students:

            self.students[name].update(new_marks)
            self.save()
            print("Marks have update")

        else:
            print("Student not found")

    def delete_student(self,name):

        if name in self.students:

            del self.students[name] 
            self.save()
            print("Deleted Successfull")

        else:
            print("Student not found")