class Student:
    after_Age=10
    def __init__(self,name,rollno,age):
        self.name=name
        self.branch="cse"
        self.rollno=rollno
        self.age=age

    def display(self):
        print(f"Student Name:{self.name}")
        print(f"Student branch:{self.branch}")
        print(f"Student rollno:{self.rollno}")
    def add_(self):
        Age=int(input("enter the age:"))
        
 
        
        


s1=Student("malathi",712222104017,21)    

s1.display()

