from get import *

print('(c) Stam Kaly 2016. All rights reserved.\n\n')
print(db.update())
print('\n\nHow to use:\n   Use "ip = <ip>" and "tz = <time zone>" to save the values to memory for use of the commands\n\n   1. gmt2mt(<GMT time>): Converts given GMT time to your local time   Example: "gmt2mt(17:00)"\n'+"   2. gmt2lt(<GMT time>): Converts given GMT time to saved IP'"+ 's local time   Example: "gmt2lt(17:00)"\n   3. gmt2lt2(<GMT time>): Converts given GMT time to saved time zone'+ "'" + 's local time   Example: "gmt2lt2(17:00)"\n   4. ip2lt: Returns the local time of the saved IP   Example: "ip2lt"\n   5. ip2lt2: Returns the local time of the saved time zone   Example: "ip2lt2"\n\nType "help" to view this again!\nHave fun converting!')
x = ''

def helpf():
    print('How to use:\n   Use "ip = <ip>" and "tz = <time zone>" to save the values to memory for use of the commands\n\n   1. gmt2mt(<GMT time>): Converts given GMT time to your local time   Example: "gmt2mt(17:00)"\n'+"   2. gmt2lt(<GMT time>): Converts given GMT time to saved IP'"+ 's local time   Example: "gmt2lt(17:00)"\n   3. gmt2lt2(<GMT time>): Converts given GMT time to saved time zone'+ "'" + 's local time   Example: "gmt2lt2(17:00)"\n   4. ip2lt: Returns the local time of the saved IP   Example: "ip2lt"\n   5. ip2lt2: Returns the local time of the saved time zone   Example: "ip2lt2"\n\nType "help" to view this again!\nHave fun converting!')

def lookup(x):
    if (x.startswith("gmt2mt(") is True and x.endswith(")") is True and len(x) == 13 and x[9] == ":"):
        try:
            print(localt.gmt2mt(str(int(x[7:9])), str(int(x[10:12]))))
        except ValueError:
            print("Please input time!")
    elif (x.startswith("gmt2lt(") is True and x.endswith(")") is True and len(x) == 13 and x[9] == ":"):
        try:
            print(localt.gmt2lt(str(ip), str(int(x[7:9])), str(int(x[10:12]))))
        except ValueError:
            print("Please input time!")
    elif (x.startswith("gmt2lt2(") is True and x.endswith(")") is True and len(x) == 14 and x[10] == ":"):
        try:
            print(localt.gmt2lt2(str(tz), str(int(x[8:10])), str(int(x[11:13]))))
        except ValueError:
            print("Please input time!")
    elif (x == "ip2lt"):
        print(localt.ip2lt(str(ip)))
    elif (x == "ip2lt2"):
        print(localt.ip2lt2(str(tz)))


while x not in ['q']:
    try:
        x = input(">>> ")
    except EOFError:
        print ('')
        break
    if x != '':        
        if (x.startswith('ip = ') is True):
            ip = x[5:]
        if (x.startswith('tz = ') is True):
            tz = x[5:]
        if (x == "exit"):
            exit()
        if (x == "help"):
            helpf()
        lookup(x)

