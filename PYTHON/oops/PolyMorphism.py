class Employee:
   
    def Work(self):
        print("working")
       
class developer(Employee):
    def Work(self):
       print("Developing")
class HR(Employee):
    
       print("Interview Conducted")
class DA(Employee):
    def Work(self):
       print("Analysis")

Employee1=[HR(),DA(),developer()]

for emp in Employee1:
    return emp

da=HR()
da.Work()