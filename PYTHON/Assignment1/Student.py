#Accept:

#Student Name
#Age
#Degree
#Percentage
#Display details.

#Determine eligibility:

#Percentage >= 60 → Eligible
#Percentage < 60 → Not Eligible
#Calculate:

#Years remaining to reach age 30
#Percentage required to reach 100

Name=input("Enter the Student Name:")
Age=int(input("Enter the Age:"))
Degree=input("Enter the Degree:")
per=float(input("Enter the Mark"))
Percentage=(per/100)*100

print(f"Student Name:{Name}")
print(f"Age:{Age}")
print(f"Degree:{Degree}")
print(f"Percentage:{Percentage}")

if Percentage>=60:
    print("Eligible")
else:
    print("Not Eligible")


remaining_year=30-Age
print(f"remaining year:{remaining_year}")

Percentage_Requirement=100-Percentage
print(f"Percentage:{Percentage_Requirement}")




