sales = [12000, 15000, 18000, 9000, 21000, 17000]

 #Calculate Total Sales

def calculate_total_sales(sale):
    return sum(sale)
print(calculate_total_sales(sales))  

def Average_sales(sale):
    avg=sum(sale)/len(sale)
    return avg
print(Average_sales(sales))


def find_highest_sale(sale):
    return max(sale)
print(find_highest_sale(sales))

def find_lowest_sale(sale):
    return min(sale)
print(find_lowest_sale(sales))



#Function Arguments & Return Values

def sales_growth(current_month, previous_month):
    if previous_month==0:
        return 0
    growth=((current_month-previous_month)/previous_month)*100
    return f"{growth}%"
print(sales_growth(25000,20000))


#2. Convert Customer Names to Uppercase

customers = ["john", "mary", "david"]
customer_upper=[]
for cus in customers:

       customer_upper.append(cus.upper())

print(customer_upper)

#sorted()
sort=lambda sales:sorted(sales)
print(sort(sales))

#Create a recursive countdown:




#factorial(n)
n=5
fact=1
def factorial(n,fact):
    while(n>0):
       fact=fact*n
       n=n-1
    return fact
print(factorial(n,fact))




#Create a recursive countdown:
countdown=int(input("CountDown: "))
for i in range(countdown,0,-1):
 print(i)



#What is the total sales revenue?
print(f"Total Sales:{calculate_total_sales(sales)} ")
#What is the average sales value?
print(f"Average Sales:{Average_sales(sales)}")
#What is the highest sale recorded?
print(f"Higest Sale:{find_highest_sale(sales)}")
#What is the lowest sale recorded?
print(f"Lowest Sale:{find_lowest_sale(sales)}")
#What is the sales growth percentage compared to the previous month?
import datetime
print(f"current_date:{datetime.datetime.now()}")

#What business actions would you recommend based on the sales performance
print(f"Growth:{sales_growth(25000,20000)}")


    

