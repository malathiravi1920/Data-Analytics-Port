class Employee:
    def work(self):
        print("Working")
class Manager(Employee):
    pass
m=Manager()

m.work()
