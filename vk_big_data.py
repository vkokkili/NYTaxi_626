import csv, time
from datetime import datetime
import matplotlib.pyplot as plt
import operator

start = time.time()

fn= 'trip_data_1.csv'
f= open(fn,"r") #create a file handle to open csv
reader =  csv.reader(f)
n=0 #count rows
x = 0
min_pickup_time = None
max_dropoff_time = None
min_pickup_longitude = None
max_pickup_longitude = None
min_pickup_latitude = None
max_pickup_latitude = None
min_trip_dist = None
max_trip_dist = None
min_trip_time = None
max_trip_time = None
pc=0
total_rides={}
total_passenger={}
vendorid, ratecode = set(), set()
f1 = open('output.csv', 'w') #open the file in write mode
f1= open('output.csv','a') #open the file in append mode
writer = csv.writer(f1,delimiter=',',lineterminator='\n') #creating writer object
for row in reader:
    #calculating min and max pickup and dropoff latitudes and longitudes
    if n > 1:
        if min_pickup_longitude is None:
            min_pickup_longitude = float(row[10])
        else:
            if float(row[10]) >= -74.0229587 and float(row[10])<= -73.9114409:
                if min_pickup_longitude > float(row[10]):
                    min_pickup_longitude = float(row[10])

        if max_pickup_longitude is None:
            max_pickup_longitude = float(row[10])
        else:
            if float(row[10]) >= -74.0229587 and float(row[10])<= -73.9114409:
                if max_pickup_longitude < float(row[10]):
                    max_pickup_longitude = float(row[10])


        if min_pickup_latitude is None:
            min_pickup_latitude = float(row[11])
        else:
            if float(row[11]) >= 40.7994684 and float(row[11])<= 40.8732995:
                if min_pickup_latitude > float(row[11]):
                    min_pickup_latitude = float(row[11])

        if max_pickup_latitude is None:
            max_pickup_latitude = float(row[11])
        else:
            if float(row[11]) >= 40.7994684 and float(row[11])<= 40.8732995:
                if max_pickup_latitude < float(row[11]):
                    max_pickup_latitude = float(row[11])

        #calculating min and max values for trip distance
        if min_trip_dist is None and row[9] != '' and float(row[9]) != 0.0:
            min_trip_dist = float(row[9])
        else:
            if min_trip_dist > float(row[9]) and row[9] != '' and float(row[9]) != 0.0:
                min_trip_dist = float(row[9])

        if max_trip_dist is None and row[9] != '' and float(row[9]) != 0.0:
            max_trip_dist = float(row[9])
        else:
            if max_trip_dist < float(row[9]) and row[9] != '' and float(row[9]) != 0.0:
                max_trip_dist = float(row[9])

        
        #calculating min and max values for trip time in secs
        if row[8]!='':
            if min_trip_time is None and float(row[8]) != 0.0:
                min_trip_time = float(row[8])
            else:
                if min_trip_time > float(row[8]) and float(row[8]) != 0.0:
                    min_trip_time = float(row[8])

            if max_trip_time is None:
                max_trip_time = float(row[8])
            else:
                if max_trip_time < float(row[8]):
                    max_trip_time = float(row[8])
        datetime = datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S')
        htime = datetime.hour
        passenger_count = row[7]

        if htime in total_rides.keys():
            total_rides[htime]+=1
        else:
            total_rides[htime]=1

        if htime in total_passenger.keys():
            pc =  pc + int(passenger_count)
            total_passenger[htime]=pc
        else:
            total_passenger[htime]=pc

        sorted_rides = sorted(total_rides.items(), key=operator.itemgetter(0),reverse=True)
        sorted_passenger_count = sorted(total_passenger.items(), key=operator.itemgetter(0),reverse=True)
        #Now idea is to divide the passenger_count with total_rides by hour


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
        writer.writerow(row) #creating a writer object
    n+=1
    if n == 1:
        print(" \n")
        print("column names:",row)
        print(" \n")
    #print sample data for each field
    if n > 1 and n < 6:
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
#min and max pickup longitude and pickup latitude
print("Minimum pickup longitude:", min_pickup_longitude,"Maximum pickup longitude:", max_pickup_longitude)
print("Minimum pickup latitude:", min_pickup_latitude, "Maximum pickup latitude:", max_pickup_latitude)
print("Minimum trip distance:", min_trip_dist,"Maximum trip distance:", max_trip_dist)
print("Minimum trip time:", min_trip_time,"Maximum trip time:", max_trip_time)

f1.close()

plt.bar(total_rides.keys(), total_rides.values(), color='green')
plt.title('Total rides by hour')
plt.xlabel('Hour')
plt.ylabel('Ride Count')
plt.show(block=False)
plt.pause(20)
plt.close()
plt.bar(total_passenger.keys(), total_passenger.values())
plt.title('Total number of passengers by hour')
plt.xlabel('Hour')
plt.ylabel('Passenger Count')
plt.show(block=False)
plt.pause(20)
plt.close()
#print("Total rides in hour:", total_rides)
print("sorted rides by hour:", sorted_rides)
print("\n")
print("sorted passenger count by hour:", sorted_passenger_count)
#print("Total passenger count:", total_passenger)
print(time.time() - start)
