import time
#You are given the following information, but you may prefer to do some research for yourself.
#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

#Them Variables
year = 1901 #I had this set to 1900, and I'm an idiot.
month = 1
day = 1
weekDay = 2 #1: Monday 2: Tuesday 3: Wednesday 4: Thursday 5: Friday 6: Saturday 7: Sunday
weekDayList = ["Placeholder","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
#^^ This list just makes it look nicer. THe first element is "Placeholder" because I never use the 0th index in the code

didDayChange = False #This is to try and get around the issue of a day not being added after Sunday
didWeekDayChange = False #Pretty much does the same thing

sundayCount = 0

def dayChecker(weekDay): #Checks if it's a Sunday, and starts a new week if it is
    if weekDay == 7:
        didWeekDayChange = True #Registers that the weekday has changed in this iteration
    
    else:
        didWeekDayChange = False
    return didWeekDayChange


while year <= 2000:
    print("Today is", weekDayList[weekDay], ",", str(month),"/",str(day),"/",str(year))
    
    if weekDay == 7 and day == 1:
        sundayCount += 1
        print("Sunday Counter is at:",str(sundayCount))

    if dayChecker(weekDay) == True:
        weekDay = 0 #Not sure why I need to do this, but for some reason the code keep skipping Monday.
        didWeekDayChange = True
    else:
        didWeekDayChange = False
  
     

    #Thirty Days Hath September...
    if (month == 9 or month == 4 or month == 6 or month == 11) and day == 30:
        month += 1
        day = 1
        if dayChecker(weekDay) == False:
            weekDay += 1
        didDayChange = True #Registers that the day has changed in this iteration
        didWeekDayChange = True #Registers that the weekday has changed in this iteration
        next
        
               
    #February had to go and be different. Nice going, February. -_-
    elif month == 2 and day == 28:
        #Checks for a leap year
        if year % 4 == 0 and year > 1900:
            day += 1

            if dayChecker(weekDay) == False:
                weekDay += 1
            didDayChange = True
            didWeekDayChange = True

            #This block is weird. Due to the bizarre nature of leap year, when it is leap year, this block advances
            #Time forward two days instead of one.
            print("Today is", weekDayList[weekDay], ",", str(month),"/",str(day),"/",str(year))
            day = 1
            month += 1
            if weekDay == 7:
                weekDay = 1
            else:
                weekDay += 1
            next

        else:    
            day = 1
            month += 1
            if dayChecker(weekDay) == False:
                weekDay += 1
            didDayChange = True
            didWeekDayChange = True
            next

    #If the previous block registers that it is a leap year, it will jump here at the next iteration     
    elif month == 2 and day == 29:
        day = 1
        month += 1
        if dayChecker(weekDay) == False:
            weekDay += 1
        didDayChange = True
        didWeekDayChange = True
        next
     
    #All the rest have 31...
    elif day == 31:
        month += 1
        day = 1
        if dayChecker(weekDay) == False:
            weekDay += 1
        if month == 13: #If it's currently December when the code reaches this, month += 1 will temporarily make an imaginary month 13
            year += 1
            month = 1
        didDayChange = True
        didWeekDayChange = True
        next
    
    else:
        didDayChange = False
        if dayChecker(weekDay) != True:
            didWeekDayChange = False
           
        
        
            
        
    if didDayChange == False:
        day += 1
    
    if didWeekDayChange == False:
        weekDay += 1



        
      
print("There were",sundayCount,"Sundays on the first of a month!")



