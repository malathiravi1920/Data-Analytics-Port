#import csv
#with open(r"C:\Users\ELCOT\Data Analytics Port\PYTHON\FileHandling\data.csv",'r') as file:
 #   reader=csv.reader(file)
  #  for  row in reader:
   #     print(row)

#import csv
#with open(r"C:\Users\ELCOT\Data Analytics Port\PYTHON\FileHandling\data.csv",'w',newline='') as file:
 #   writer=csv.writer(file)
  #  writer.writerow(["ink",25])
   # writer.writerow(["pen",20])


import csv 
total_sales=0
Average=0
with open(r"C:\Users\ELCOT\Data Analytics Port\PYTHON\FileHandling\data.csv",'r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        total_sales=int(row['sales'])
        print(total_sales)
        number=int(len(row))
    
    Average=total_sales/number
    print(Average)


    