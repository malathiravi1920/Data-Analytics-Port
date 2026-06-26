Excellent=0
Good=0
total=0
improvement_required=0

for i in range(1,11):
    Attendance=int(input(f"enter the Attendance{i}:"))
    if Attendance<0:
      break
    elif Attendance==0:
       pass
    elif Attendance>100:
       continue
   
#Summary
#Calculate and display:
    total+=0
#Total Employees Processed

    if Attendance>=90:
        Excellent+=1
       
#Number of Excellent Employees
#Number of Good Employees
    elif Attendance>75:
        Good+=1
        
#Number of Employees Requiring Improvement

    else:
        improvement_required+=1
       
print(f"Employee {i}:Excellent")
print(f"Employee {i}:Good")
print(f"Employee {i}:improvement_required")
print("\nAttendance Summary")
print(f"Total Employees Processed:{total}")
print(f"Excellent:{Excellent} ")
print(f"Good:{Good}")
print(f"Improvement:{improvement_required}")
   

      
      
      
        



    

    