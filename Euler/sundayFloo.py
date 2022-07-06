didWeekDayChange = False
weekDay = 7
def dayChecker(weekDay): #Checks if it's a Sunday, and starts a new week if it is
    if weekDay == 7:
        didWeekDayChange = True #Registers that the weekday has changed in this iteration
        weekDay = 1
    else:
        didWeekDayChange = False
    print(weekDay)
    return didWeekDayChange


if dayChecker(weekDay) == True:
    print("It works!")
    print(weekDay)

