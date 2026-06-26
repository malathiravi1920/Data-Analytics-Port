from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def Work(self):
        print("working")
       
class developer(Employee):
    def Work(self):
       print("Developing")
class HR(Employee):
    
        print("Interview Conducted")
class DA(Employee):
    def Work(self):
        pass

da=HR()
da.Work()