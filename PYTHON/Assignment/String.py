#Convert the name to uppercase.
#Convert the name to lowercase.
#Remove leading and trailing spaces.
#Count the number of characters.
#Check whether a specific word exists in the customer name.

name=" Join Smith "
print(name.upper())
print(name.lower())
print(name)
leng=len(name)
print(f" length:{leng}")

#list
#Add a new customer.
#Remove a customer.
#Sort customers alphabetically.
#Display total number of customers.
#Display the first and last customer.
#output
customers = ["John", "Mary", "David"]
print(customers)

customers.append("Jothi")
print(customers)

customers.remove("John")
print(customers)

customers.sort()
print(customers)

customers = ["John", "Mary", "David"]
total_count=0
total_count=len(customers)
print(f"total number of customer:{total_count}")

first=customers[0]
print(first)

last=customers[-1]
print(last)


#information:

#Company Name
#Location
#Establishment Year


#Tasks:

#Display all values.
#Access individual elements.
#Display company age.

#Example:

company = ("ABC Support Services", "Coimbatore", 2015)
print(company)
for com in company:
    print(com)
start_yaer=company[2]
current_year=2026
company_age=current_year-start_yaer
print(f"comapny age is:{company_age}")


#Tasks:

#Display all unique cities.
#Count unique cities.
#Add a new city.
#Remove a city.
#Check whether a city exists.

cities = {"Chennai", "Coimbatore", "Madurai", "Chennai"}
print(cities)
unique=len(cities)
print(unique)
cities.add("Ariyalur")
print(cities)
cities.remove("Ariyalur")
print(cities)
cities.discard("Ariyalur")
print(cities)



#Tasks:

#Display all customer details.
#Update satisfaction rating.
#Add a new field:
#Membership Type
#Remove a field.
#Display all keys and values separately.

customer1 = {
    "Customer_ID": "C101",
    "Name": "John",
    "City": "Chennai",
    "Satisfaction_Rating": 4.5
}

print(customer1)
customer1.update({"Satisfaction_Rating": 5.5})
print(customer1)
customer1["Product"]="Laptop"
print(customer1)

for customer in customer1:
    print(customer)

for key,value in customer1.items():
    print(f"{key}:{value}")

customer1.popitem()
print(customer1)

for key in customer1:
    print(key)
for value in customer1.values():
    print(value)

print("Customer Summary Report")
#How many customers are stored in the system?
print(f"Total Customers:{total_count}")
#How many unique cities are represented?
print(f"Unique Cities:{unique}")
#Which customer has the highest satisfaction rating?
#Generate a simple customer summary report.
#Identify duplicate customer cities and store only unique cities.
print("Cities:")
for key in cities:
    print(key)


print("Company:")
for com in company:
    print(com)

