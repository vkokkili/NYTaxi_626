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