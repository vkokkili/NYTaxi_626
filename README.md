# NYTaxi_626
 
**NY Taxi data analysis - IA626**

In this project we will analyze a dataset which contains information about taxi rides in NYC.  The data set is quite large so getting a basic idea of what the data contains is important.  Each student should use one of the CSV files.  Answer the following questions:

1. What time range does your data cover?  How many rows are there total?
1. What are the field names?  Give descriptions for each field.
1. Give some sample data for each field.
1. What MySQL data types would you need to store each of the fields?
int(xx), varchar(xx),date,datetime,bool, decimal(m,d)
1. What is the geographic range of your data (min/max - X/Y)?
1. Plot this (approximately on a map)
1. What are the distinct values for each field? (If applicable)
1. For other numeric types besides lat and lon, what are the min and max values?
1. Create a chart which shows the average number of passengers each hour of the day.
1. Create a new CSV file which has only one out of every thousand rows.
1. Repeat step 8 with the reduced dataset and compare the two charts.


**Dataset used: trip_data_1.csv**

*Imports used*
```
import csv, time
from datetime import datetime
import matplotlib.pyplot as plt
%matplotlib inline
```

The data file used for this assignment is huge ~2.5GB. To make it faster and efficient, the following method is used to read the file from the disk.

*Creating a file handle to open the csv data file*
```
fn= 'trip_data_1.csv'
f= open(fn,"r")
reader =  csv.reader(f)
```

*Initializing variables which will be used to answer the questions above*
```
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

** Answers to questions above **
*What time range does your data cover?  How many rows are there total?

The time range that needs to be calculated is: the minimum pickup_datetime and the maximum pickup_datetime value. The code used to calculate these values is as below:

```
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

```
n = 0
for row in reader:
    n += 1
print("Total number of rows (without header):", n-1)
```
Output:

![Output for total row count](/Images/TotalRows.png)


*What are the field names?  Give descriptions for each field.
Field names are nothing but headers in the first row from the csv file. This is basically the 0th index.

Output:

![Output for field names](/Images/FieldNames.png)

Here are the field descriptions after some research done over the internet:

Field Name | Description
------------ | -------------
medallion  | A taxi medallion, also known as a CPNC (Certificate of Public Necessity and Convenience), is a transferable permit in the United States allowing a taxicab driver to operate
hack_license  | A New York City Taxi Drivers License
vendor_id | A designation for the vendor that provided the record. CMT=Creative Mobile Technologies VTS= VeriFone, Inc. DDS=Digital Dispatch Systems
rate_code | The final rate code in effect at the end of the trip. 1= Standard rate 2=JFK 3=Newark 4=Nassau or Westchester 5=Negotiated fare 6=Group ride
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

