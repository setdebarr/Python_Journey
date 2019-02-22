#!/usr/bin/env python3

import decimal

#Checks to make sure user input is valid
while True:
    try:
        n = int(input("Enter the number of decimal places you want to see: "))
        if n < 1 or n > 1000:
            raise ValueError #This will send it to the print message and back to the input option
        break
    except ValueError:
        print("Oops!  That number was to high.  Try again...")

def factorial(n):
    factorials = [1]
    for i in range(1, n + 1):
        factorials.append(factorials[i - 1] * i)
    return factorials

#brothers' formulae
def compute_e(n):
    decimal.getcontext().prec = n + 1
    e = 2
    factorials = factorial(2 * n + 1)
    for i in range(1, n + 1):
        counter = 2 * i + 2
        denominator = factorials[2 * i + 1]
        e += decimal.Decimal(counter / denominator)
    return e

print(str(compute_e(n)))