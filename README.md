# NYTaxi_626
 
**NY Taxi data analysis - IA626**

In this project we will analyze a dataset which contains information about taxi rides in NYC.  The data set is quite large so getting a basic idea of what the data contains is important.  Each student should use one of the CSV files.  Answer the following questions:

1. What time range does your data cover?  How many rows are there total?
1. What are the field names?  Give descriptions for each field.
1. Give some sample data for each field.
1. What MySQL data types would you need to store each of the fields?
int(xx), varchar(xx),date,datetime,bool, decimal(m,d)
1. What is the geographic range of your data (min/max - X/Y)? Plot this (approximately on a map)
1. What are the distinct values for each field? (If applicable)
1. For other numeric types besides lat and lon, what are the min and max values?
1. Create a chart which shows the average number of passengers each hour of the day.
1. Create a new CSV file which has only one out of every thousand rows.
1. Repeat step 8 with the reduced dataset and compare the two charts.


**Dataset used: trip_data_1.csv**

*Imports used*
```python
import csv, time
from datetime import datetime
import matplotlib.pyplot as plt
%matplotlib inline
```

The data file used for this assignment is huge ~2.5GB. To make it faster and efficient, the following method is used to read the file from the disk.

*Creating a file handle to open the csv data file*
```python
fn= 'trip_data_1.csv'
f= open(fn,"r")
reader =  csv.reader(f)
```

*Initializing variables which will be used to answer the questions above*
```python
n=0
x = 0
min_pickup_time = None
max_dropoff_time = None
vendorid, ratecode = set(), set()

min_pickup_longitude = None
max_pickup_longitude = None
min_pickup_latitude = None
max_pickup_latitude = None

min_dropoff_longitude = None
max_dropoff_longitude = None
min_dropoff_latitude = None
max_dropoff_latitude = None

min_trip_time = None
max_trip_time = None
```

## Answers to questions above ##
---
#### 1) What time range does your data cover?  How many rows are there total?####

The time range that needs to be calculated is: the minimum pickup_datetime and the maximum pickup_datetime value. The code used to calculate these values is as below:

```python
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
```
Output:

![Output for date range](/Images/DateRange.png)


And to calculate the number of rows in the data file trip_data_1.csv, this was achieved by incrementing the counter 'n' and making sure that the header row in the csv is not included.

```python
n = 0
for row in reader:
    n += 1
print("Total number of rows (without header):", n-1)
```
Output:

![Output for total row count](/Images/TotalRows.png)


#### 2) What are the field names?  Give descriptions for each field.####
Field names are nothing but headers in the first row from the csv file. This is basically the 0th index.

Output:

![Output for field names](/Images/FieldNames.png)

Here are the field descriptions after some research done over the internet:

Field Name | Description
------------ | -------------
medallion  | A taxi medallion, also known as a CPNC (Certificate of Public Necessity and Convenience), is a transferable permit in the United States allowing a taxicab driver to operate
hack_license  | A New York City Taxi Drivers License
vendor_id | A designation for the vendor that provided the record. CMT=Creative Mobile Technologies VTS= VeriFone, Inc. DDS=Digital Dispatch Systems
rate_code | The final rate code in effect at the end of the trip.
store_and_fwd_flag | This flag indicates whether the trip record was held in vehicle memory before sending to the vendor, aka “store and forward,” because the vehicle did not have a connection to the server. Y= store and forward trip N= not a store and forward trip
pickup_datetime |The date and time when the meter was engaged
dropoff_datetime |The date and time when the meter was disengaged
passenger_count |The number of passengers in the vehicle. This is a driver-entered value
trip_time_in_secs|Time in seconds taken to complete the trip from pickup to dropoff
trip_distance |The elapsed trip distance in miles reported by the taximeter
pickup_longitude |Longitude where the meter was engaged
pickup_latitude |Latitude where the meter was engaged
dropoff_longitude | Longitude where the meter was disengaged
dropoff_latitude | Latitude where the meter was disengaged

#### 3) Give some sample data for each field ####
Sample data was provided using the for loop statement and retriving the first 5 rows for each column.
```python
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
```

Output:

![Output for sample data](/Images/SampleData.png)

#### 4) What MySQL data types would you need to store each of the fields? ####
Based on the descriptions and sample data above, if this data was to be loaded into a MYSQL database, the following data types would be ideal to store each field within the database:

Field Name | Data Type
------------ | -------------
medallion  | Varchar(50)
hack_license  | Varchar(50)
vendor_id | Varchar(3) not null default ‘0’
rate_code | Varchar(3) not null default ‘0’
store_and_fwd_flag | varchar(1) not null default ‘N’
pickup_datetime | Datetime not null
dropoff_datetime |Datetime not null
passenger_count | smallint not null default 0
trip_time_in_secs| Int not null default 0
trip_distance | decimal(6,3) not null default 0
pickup_longitude | decimal(18,14)
pickup_latitude |decimal(18,14)
dropoff_longitude | decimal(18,14)
dropoff_latitude |decimal(18,14)

#### 5) What is the geographic range of your data (min/max - X/Y)? Plot this (approximately on a map)####

Finding minimum and maximum values for pickup longitude, pickup latitude, dropoff longitude and dropoff latitude.

Code snippet:
```python
if min_pickup_longitude is None:
            min_pickup_longitude = float(row[10])
        else:
            if min_pickup_longitude > float(row[10]):
                min_pickup_longitude = float(row[10])

        if max_pickup_longitude is None:
            max_pickup_longitude = float(row[10])
        else:
            if max_pickup_longitude < float(row[10]):
                max_pickup_longitude = float(row[10])
```
Output:

![Output for minimum and maximum values of pickup longitude](/Images/MinMaxPickupLongitude_Invalid.png)

The valid range of latitude in degrees is -90 and +90 for the southern and northern hemisphere respectively. Longitude is in the range -180 and +180 specifying coordinates west and east of the Prime Meridian, respectively. But the above output makes no sense. So, there are two options for us that needs to be considered:
1) Data cleanup to make sure the data is within the valid ranges for latitude and longitude
2) Only find minimum and maximum values within a given range for data analysis

I have chosen to go with option# 2, since data cleanup is assumed out of scope for this assignment and would take longer than expected. Data analysts usually spend months to clean up data.

Given this is NYC data, going to use the NYC (manhattan) limits for latitude and longitude, which would be
40.8732995,-73.9114409/40.7994684,-74.0229587 (based on google maps)

code with limits checking:
```python
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
```

Output:

![Output for minimum and maximum values of pickup longitude and latitude](/Images/MinMaxPickupLongLat.png)

![Minimum pickup location](/Images/MinPickup)
![Maximum pickup location](/Images/MaxPickup)




To find minimum and maximum values for trip time in seconds, the following code was implemented:
```python
if row[8]!='':
            if min_trip_time is None:
                min_trip_time = float(row[8])
            else:
                if min_trip_time > float(row[8]):
                    min_trip_time = float(row[8])

            if max_trip_time is None:
                max_trip_time = float(row[8])
            else:
                if max_trip_time < float(row[8]):
                    max_trip_time = float(row[8])
```


Output:

![Output for minimum and maximum values for trip time in secs](/Images/MinMaxTripTime_Invalid.png)

You will notice that the minimum trip time is 0.0. Which again does not make sense or says that the trip did not happen, which should not be considered. So, modified the code with the following condition check as shown below to not consider 0.0 values.

```python
if row[8]!='':
            if min_trip_time is None and float(row[8]) != 0.0:
                min_trip_time = float(row[8])
            else:
                if min_trip_time > float(row[8]) and float(row[8]) != 0.0:
                    min_trip_time = float(row[8])
```
Output:

![Output for minimum and maximum values for trip time in secs](/Images/MinMaxTripTime.png)

Similar to Trip time above, the data file has zero and empty string trip distance values. The following code is used to eliminate those values and find minimum and maximum values for trip distance.

```python
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
```

Output:

![Output for minimum and maximum values for trip distance](/Images/MinMaxTripDistance.png)




