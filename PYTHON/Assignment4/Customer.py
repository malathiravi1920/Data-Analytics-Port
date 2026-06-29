#with open(r"C:\Users\ELCOT\Data Analytics Port\PYTHON\Assignment4\company_notice.txt","r") as file:
#    data=file.read()
#print(data)

import csv
with open(r"C:\Users\ELCOT\Data Analytics Port\PYTHON\Assignment4\Feedback.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

import csv
with open(r"C:\Users\ELCOT\Data Analytics Port\PYTHON\Assignment4\feedback_summary.txt","w") as file:
   file.write("append")

   #The report should contain:

#Total Customers

#Valid Ratings
#Invalid Ratings
#Average Rating

import csv 
total_customer=0
Average_Rating=0
Invalid_Rating=0
Valid__Rating=0
with open(r"C:\Users\ELCOT\Data Analytics Port\PYTHON\Assignment4\FeedBack.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        total_customer=row["Customer_ID"]
        print(total_customer)
       
