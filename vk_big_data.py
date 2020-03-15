import csv, time
from datetime import datetime

start = time.time()

fn= 'trip_data_1.csv'
f= open(fn,"r") #create a file handle to open csv
reader =  csv.reader(f)
n=0 #count rows
x = 0
min_pickup_time = None
max_dropoff_time = None
vendorid, ratecode = set(), set()
f1 = open('output.csv', 'w')
f1= open('output.csv','a')
writer = csv.writer(f1,delimiter=',',lineterminator='\n')
for row in reader:
    if n > 0:
        pickuptime = datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S')
        if min_pickup_time is None:
            min_pickup_time = pickuptime
        elif pickuptime < min_pickup_time:
            min_pickup_time = pickuptime

        # finding highest value of dropoff datetime
        dropofftime = datetime.strptime(row[6], '%Y-%m-%d %H:%M:%S')
        if max_dropoff_time is None:
            max_dropoff_time = dropofftime
        elif dropofftime > max_dropoff_time:
            max_dropoff_time = dropofftime

    if n % 1000 == 0:
        writer.writerow(row)
    n+=1
    if n == 1:
        print(" \n")
        print("column names:",row)
        print(" \n")
    #print sample data for each field
    if n > 0 and n < 6:
        print("=====Set#",x+1, "====")
        print("Medallion sample data:", row[0])
        print("Hack License sample data:", row[1])
        print("Vendor ID sample data:", row[2])
        print("Rate Code sample data:", row[3])
        print("Store and fwd flat sample data:", row[4])
        print("pickup datetime sample data:", row[5])
        print("dropoff datetime sample data:", row[6])
        print("passenger count sample data:", row[7])
        print("trip time in secs sample data:", row[8])
        print("trip distance sample data:", row[9])
        print("pickup longitude sample data:", row[10])
        print("pickup latitude sample data:", row[11])
        print("dropoff longitude sample data:", row[12])
        print("dropoff latitude sample data:", row[13])
        print(" \n")
        x+=1

    if n > 1:
        if row[2] not in vendorid:
            vendorid.add(row[2])
        if row[3] not in ratecode:
            ratecode.add(row[3])



print("Distinct vendor IDs:", vendorid)
print("Distinct ratecodes:", ratecode)
print(" \n")
print("Total number of rows (without header):", n-1)
print(" \n")
# min_pickup_time
print("Minimum pickup date time:", min_pickup_time)
# max_dropoff_time
print("Maximum dropoff date time:", max_dropoff_time)
f1.close()

print("Time taken to execute this script:", time.time()-start)
