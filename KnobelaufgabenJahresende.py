from datetime import date

def Schaltjahr(jahreszahl):
    if (jahreszahl%400==0):
        return True
    elif (jahreszahl%400!=0 and jahreszahl%100==0):
        return False
    elif (jahreszahl%100!=0 and jahreszahl%4==0):
        return True
    else:
        return False

def TageSeit(tag, monat, jahr):
    def Schaltjahr(jahreszahl):
        if (jahreszahl%400==0):
            return True
        elif (jahreszahl%400!=0 and jahreszahl%100==0):
            return False
        elif (jahreszahl%100!=0 and jahreszahl%4==0):
            return True
        else:
            return False
    def increaseDateByOne(dateString):
        #dateString hat das Format dd/mm/yyyy
        dateList = dateString.split("/")
        dateList[0], dateList[1], dateList[2] = int(dateList[0]), int(dateList[1]), int(dateList[2])
        tageImMonat = None
        if Schaltjahr(dateList[2]):
            tageImMonat = {1:31, 2:29, 3:31, 4:30, 5: 31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:31, 12:31}
            
        else:
            tageImMonat = {1:31, 2:28, 3:31, 4:30, 5: 31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:31, 12:31}

        print(dateList[1])
        maxDays = tageImMonat[dateList[1]]
        dateList[0] += 1
        if (dateList[0]>maxDays):
            dateList[0] = 1
            dateList[1] += 1
        if (dateList[1]>12):
            dateList[1] = 1
            dateList[2] += 1
        return str(dateList[0]) + "/" + str(dateList[1]) + "/" + str(dateList[2])
    
    today = date.today().strftime("%d/%m/%Y")
    enteredDate = str(tag) + "/" + str(monat) + "/" + str(jahr)
    dayCounter = 0
    while True:
        if (enteredDate==today):
            break
        else:
            dayCounter += 1
            enteredDate = increaseDateByOne(enteredDate)

    return dayCounter

def Quersumme(zahl):
    zahl = str(zahl)
    sum = 0
    for i in zahl:
        sum += int(i)
    return sum
    
