try:

    age=int(input("Enter the age"))
    print(age)
except ValueError:
    print("Invalid Age")
except SyntaxError:
    print("Invalid Syntax")

try:
    print("process")
except:
    print("error")
finally:
    print("completed")


try:
    o=open(r"C:\Users\ELCOT\Data Analytics Port\PYTHON\FileHandling\data.csv",'r')
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution Completed")
    