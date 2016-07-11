import csv




def ip(ip):
    with open("./get/ip-timezone/ip-timezone.csv") as f:
        for row in csv.reader(f):
            for list in row:
                if ip in list:
                    return row[1]
