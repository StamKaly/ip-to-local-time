# IP to Local Time

This is my first project with time and a small reason I made it is to get a feel
of the language.
It has 2 basic functions:
* Getting the local time of any location in the world (needs IP)
* Converting yours or anyone's local time into GMT/UTC (needs IP unless you are converting your time)


## Installing requirements and launching

It's very easy and straightforward just run the following command:
```
pip install -r requirements.txt
```
Then run [main.py](http://github.com/StamKaly/ip-to-local-time/blob/master/main.py) to launch it. You can also use it as a module for your
own code! View below...


## Databases

The code is using 2 different databases:
* Time zones database which is offered to us by geoip
* An editable, CSV time zones [database](http://github.com/StamKaly/ip-to-local-time/blob/master/get/ip-timezone/ip-timezone.csv)

They both have the same usage, but the reason we actually use the second one is because
some IPs aren't in the big database by geoip and that causes an error in the code. 
So if you get an error by just using the 1st database, go ahead and add the IP with its
timezone in simple CSV format in the second database.


## Example usage as a module

You may only need to use [get.localt](http://github.com/StamKaly/ip-to-local-time/blob/master/get/localt.py).
```
>>> from get import *
>>> print(localt.ip2lt("46.101.20.237")) # Print local time of the IP
12:07
>>> print(localt.ip2lt("95.95.105.53")) # Using an IP which can't be detected by the basic database but it is in the CSV one
12:09
>>> print(localt.ip2lt2("Europe/London")) # Print local time of a time zone
12:10
>>> print(localt.gmt2mt("17", "00")) # Convert and print given GMT/UTC time(hours, minutes) in your local time.
20:00
>>> print(localt.gmt2lt("46.101.20.237", "17", "00")) # Convert and print given GMT/UTC time(hours, minutes) in IP's time.
18:00
>>> print(localt.gmt2lt2("US/Eastern", "17", "00")) # Convert and print given GMT/UTC time(hours, minutes) in time zone's time.
13:00
```
