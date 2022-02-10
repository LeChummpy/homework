import random

#----------------------------------------------------- 1. Ab -----------------------------------------------------------------------

def produkt(a):
    result = 1
    for i in a:
        result = result * i
    return result

def dreiNullen(a):
    countNull=0
    for i in a:
        if i==0:
            countNull+=1

    if countNull<3:
        return False
    else:
        return True
        
def groesstePrimzahl(a):
    def checkIfPrime(n):
        if n==1:
            return False
        for i in range(1, n):
            if i!=1:
                if n%i==0: #Wenn Zahl teilbar
                    return False
        return True

    primes=[]

    for i in a:
        if checkIfPrime(i):
            primes.append(i)
    primes.sort()
    if not primes:
        return None
    else:
        return primes[-1]
            
def AnzahlZeichen(text, z):
    anzahl_zeichen=0
    for i in text:
        if i==z:
            anzahl_zeichen+=1
    return anzahl_zeichen
    

def fibonacci(n):

    F_minus_two=1
    F_minus_one=1
    
    for i in range(1, n+1):
        if (i==1 or i==2):
            print(str(i) + ": 1")
            
        else:
            F=F_minus_one+F_minus_two
            print(str(i) + ": " + str(F))
            F_minus_two=F_minus_one
            F_minus_one=F

#----------------------------------------------------- 2. Ab -----------------------------------------------------------------------

def Aufgabe2():
    list=[4,5,23,4,5,4,3,4,5,4]
    sum=0
    for i in list:
        sum=sum+i
    print(sum)

def Aufgabe3():
    list=[4,5,23,4,5,4,3,4,5,4]
    
    def getMaxOfList(liste):
        for i in liste:
            currentMax=i
        
            for j in liste:
                if not(i>=j):
                    currentMax=None
                    break
            if not(currentMax==None):
                return currentMax
        
    def getMinOfList(liste):
        for i in liste:
            currentMin=i
        
            for j in liste:
                if not(i<=j):
                    currentMin=None
                    break
            if not(currentMin==None):
                return currentMin

    print("Maximum: " + str(getMaxOfList(list)))
    print("Minimum: " + str(getMinOfList(list)))

def Aufgabe4():
    liste=[]
    for i in range(6000):
        liste.append(random.randint(1, 6))

    numbers=[0,0,0,0,0,0]

    for j in liste:
        if j==1:
            numbers[0]+=1
        elif j==2:
            numbers[1]+=1
        elif j==3:
            numbers[2]+=1
        elif j==4:
            numbers[3]+=1
        elif j==5:
            numbers[4]+=1
        elif j==6:
            numbers[5]+=1

    for i in range(len(numbers)):
        print("Anzahl " + str(i+1) + ": " + str(numbers[i]))

            
def Aufgabe5():
    liste=[]
    while True:
        Eingabe=input("Note: ")
        if Eingabe=="0":
            break
        else:
            liste.append(Eingabe)

    sum_of_elements=0
    for i in liste:
        sum_of_elements+=int(i)

    average=sum_of_elements/len(liste)
    print(average)

def Aufgabe6a():
    string=input("String: ")
    anzahl_spaces=0
    for i in string:
        if i==" ":
            anzahl_spaces+=1
    print(anzahl_spaces)

def Aufgabe6b():
    string=input("String: ")
    new_string=""
    for i in string:
        if i=="e":
            new_string+="x"
        else:
            new_string+=i
    print(new_string)
        
