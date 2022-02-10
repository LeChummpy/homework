def loeffelsprache(text):
    TEXT = text.upper()
    result = []
    RESULT = ""

    for i in TEXT:
        
        if (i == "A" or i == "I" or i == "E" or i == "O" or i == "U"):
            result.append("AW" + i)
            
        else:
            result.append(i)

    return RESULT.join(result)


def tagebisferien(current_day, current_month, current_year):
    #returns null if given date is grater than specified holidays
    
    result = 0

    def NumberOfDaysInCurrentMonth(month, leap_year):

        if (leap_year==True):
            if (month==1):
                return 31

            elif (month==2):
                return 29

            elif (month==3):
                return 31

            elif (month==4):
                return 30

            elif (month==5):
                return 31

            elif (month==6):
                return 30

            elif (month==7):
                return 31

            elif (month==8):
                return 31
            elif (month==9):
                return 30
            elif (month==10):
                return 31
            elif (month==11):
                return 30

            elif (month==12):
                return 31

        else:
            if (month==1):
                return 31

            elif (month==2):
                return 28

            elif (month==3):
                return 31

            elif (month==4):
                return 30

            elif (month==5):
                return 31

            elif (month==6):
                return 30

            elif (month==7):
                return 31

            elif (month==8):
                return 31
            elif (month==9):
                return 30
            elif (month==10):
                return 31
            elif (month==11):
                return 30

            elif (month==12):
                return 31
            
    ferienbeginn_tag = 12
    ferienbeginn_monat = 10
    ferienbeginn_jahr = 2020

    if (current_day==ferienbeginn_tag and current_month==ferienbeginn_monat and current_year==ferienbeginn_jahr):
        return 0
    
    elif ( (current_day>ferienbeginn_tag and current_month==ferienbeginn_monat and current_year==ferienbeginn_jahr) or (current_month>ferienbeginn_monat and current_year==ferienbeginn_jahr) or (current_year>ferienbeginn_jahr)):
        return None

    else:

        iterate_day = current_day
        iterate_month = current_month
        iterate_year = current_year
        while(True):
            result+=1

            iterate_day+=1 #day increment

            if (iterate_year%4==0): #If leap year
                if (iterate_day>NumberOfDaysInCurrentMonth(iterate_month, True)): #month increment
                    iterate_month+=1
                    iterate_day = 1
                    
            else: #if not leap year
                if (iterate_day>NumberOfDaysInCurrentMonth(iterate_month, False)):  #month increment
                    iterate_month+=1 
                    iterate_day = 1


            if(iterate_month>12):
                iterate_month=1
                iterate_year+=1

            if (iterate_day==ferienbeginn_tag and iterate_month==ferienbeginn_monat and iterate_year==ferienbeginn_jahr):
                return result


def Errechnen_von_allgemeiner_Note(Noten_Kl:[], Noten_At:[])-> int:

    '''
    Vor.: -Noten_Kl- und -Noten_At- sind Listen ausschließlich mit Elementen des Typs integer.
    Erg.: Die allgemeine Note in einem Fach ist als integer geliefert.
    '''

    def errechneNote_KlTeil(Noten:[]): #Mit Wichtung
        summe = 0

        for i in Noten:
            summe += i

        result = summe/len(Noten)
        return int(round(result, 0))

    def errechneNote_AtTeil(Noten:[]): #Mit Wichtung
        summe = 0

        for i in Noten:
            summe += i

        result = summe/len(Noten)
        return int(round(result, 0))*2

    result = ( ( errechneNote_KlTeil(Noten_Kl) + errechneNote_AtTeil(Noten_At) ) / 3 )
    return int(result)
        
        
        


        
        
