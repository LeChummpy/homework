# Autor: J. Ostrzinski
# Datum: 04.04.2019
# Zweck: Sortierverfahren (gesammelt)

from time import *
from random import *

def bubblesort(a):
   # Vor.: a ist eine Zahlenliste
   # Eff.: a ist nun aufsteigend sortiert. (Also: in-place!)
   b = len(a)-1
   for i in range(b):
      for j in range(b-i):
         if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
   return(a)
#----------------------------------------------------------------------------------
def insertsort(a):
   # Vor.: a ist eine Zahlenliste
   # Eff.: a ist nun aufsteigend sortiert. (Also: in-place!)
   for i in range(1,len(a)):
      for j in range(0,i):
         if a[i]<a[j]:
            a.insert(j,a[i])
            a.pop(i+1)
            break
   return(a)
#----------------------------------------------------------------------------------
def selectsort(a):
   # Vor.: a ist eine Zahlenliste
   # Eff.: a ist nun aufsteigend sortiert. (Also: in-place!)
   for i in range(len(a)-1):
      mini=min(a[i:])
      miniindex=a.index(mini)
      a[i],a[miniindex]=a[miniindex],a[i]
   return(a)
#----------------------------------------------------------------------------------
def mergesort(a):
   # Vor.: a ist eine Zahlenliste
   # Erg.: Eine neue Liste ist geliefert, in der die übergebene Zahlenliste nun
   #       aufsteigend sortiert ist. (Also NICHT in-place)

   def mischen(a,b):
      erg=[]
      while True:
         if len(a)==0:
            erg = erg + b
            return erg
         elif len(b)==0:
            erg = erg + a
            return erg
         else:
            if a[0]<b[0]:
               erg.append(a.pop(0))
            else:
               erg.append(b.pop(0))

   if len(a)<2:
      return a
   else:
      return mischen(mergesort(a[:len(a)//2]),mergesort(a[len(a)//2:]))
