import csv




def ip(ip):
    '''
    Returns the time zone of the IP based on the CSV database
    If the IP isn't in the database returns None
    '''
    # Open the database file
    with open("./get/ip-timezone/ip-timezone.csv") as f:
        # Load the CSV database
        for row in csv.reader(f):
            # For every line (list) in the database
            for list in row:
                # If the IP is in the line return the time zone,
                # otherwise it automatically returns None
                if ip in list:
                    return row[1]
