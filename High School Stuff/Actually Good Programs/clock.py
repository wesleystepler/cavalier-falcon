import time
hour = 12
minute = 00
second = 00
while hour <= 12:
    while minute <= 60:
        while second <= 60:
            print("The Time is:",hour,":",minute,":",second)
            second += 1
            
        second = 0
        minute += 1
    minute = 0
    if hour == 12:
        hour = 1
    else:
        hour += 1