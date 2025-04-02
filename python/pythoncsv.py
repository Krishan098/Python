import csv
# with open('persons.csv',newline='') as f:
#     csvfile=csv.reader(f)
#     for row in csvfile:
#         print(row)
with open('output.csv','w') as csv_FILE:
    csv_writer=csv.writer(csv_FILE)
    csv_writer.writerow(["Name","Age","Country"])
    csv_writer.writerow(["John Doe",30,"United States"])
    csv_writer.writerow(['Jane Doe',28,"Canada"])
with open('output.csv','a') as file:
    csv_writer=csv.writer(file)
    csv_writer.writerow(['Joe Smith',35,"United Kingdom"])
    csv_writer.writerow(['Mary Smith',32,"France"])
#Csv dialect is a set of parameters that defines the specific format of a CSV file.
with open("output.csv",'w',newline='') as file:
    csv_writer=csv.writer(file,dialect="excel")
    csv_writer.writerow(['XYZ',42,"pOIKWN"])
# Custom Dialects
my_dialect=csv.register_dialect("my_dialect",
                                delimiter=";",
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL
)
with open("output.csv",'w') as file:
    csv_writer=csv.writer(file,dialect="my_dialect")
    csv_writer.writerow(["Name","Age","Country"])
    csv_writer.writerow(['JohnDoe',30,"United States"])
import numpy as np
data=np.array([["Name","Age","Country"],
               ["John Doe",30,"United States"],
               ["Hane Doe",28,'Canada']])
np.savetxt("output_2.csv",data,delimiter=',',fmt="%s")
with open("output_2.csv",'a') as file:
    new_data= np.array([["Joe Smith",35,"United kingdom"],
                        ["Mary Smith",32,"France"]])
    np.savetxt(file,new_data,delimiter=',',fmt="%s")
    
import pandas as pd
data=pd.DataFrame([["John Doe",30,"United States"],
                   ["Jane Doe",28,"Canada"]])
data.to_csv("output.csv",index=False,header=False)