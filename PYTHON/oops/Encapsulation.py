class Employee:
    def __init__(self):
        self.__salary=50000
    def get_salary(self):#get method
        return self.__salary
    def updatesalary(self,salary):#set method
        if salary>0:
            self.__salary=salary
            return "salaty updated"
        else:
            return "invalid salary"
        
em=Employee()
print(em.get_salary())
print(em.updatesalary(10000))
print(em.get_salary())


