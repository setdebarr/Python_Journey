#!/usr/bin/env python3

from math import factorial
from decimal import Decimal, getcontext

#Checks to make sure user input is valid
while True:
    try:
        numberOfPlaces = int(input("Enter the number of decimal places you want to see: "))
        if numberOfPlaces < 1 or numberOfPlaces > 5000:
            raise ValueError #This will send it to the print message and back to the input option
        break
    except ValueError:
        print("Oops!  That was not a valid input.  Try again...")

# Chudnovsky algorithm for figuring out pi
getcontext().prec=numberOfPlaces+1
def calc(numberOfPlaces):
    t= Decimal(0)
    pi = Decimal(0)
    deno= Decimal(0)
    k=0

    t=(1)*(factorial(1))*(13591409+545140134*k)
    deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
    pi += Decimal(t)/Decimal(deno)
    pi = pi * Decimal(12) / Decimal(640320 ** Decimal(1.5))
    pi = 1/pi
    return pi

# Prints out the result
print (calc(numberOfPlaces))