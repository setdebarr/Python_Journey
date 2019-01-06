#!/usr/bin/env python3

"""
Fibonacci Sequence 
By Sean DeBarr
"""

import math
import os
import sys
import time

#Calculates the nth number
def calcNth(n):
    if n == 0:
        return 0
    a = 1
    b = 1
    c = 0
    while(n-2>0):
        c = b
        b = a + b
        a = c
        n = n - 1
    return int(b)

#Generates list to the nth number
def printList(n):
    c = []
    currentNNumber = 0
    while currentNNumber < n + 1:
        c.append(calcNth(currentNNumber))
        currentNNumber += 1
    return c

def main():
    #Program starts here
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.1)
    print("\nWELCOME TO FIBONACCI CALCULATOR / GENERATOR")
    print("\nThere are three options:")
    print("1. Calculate the nth number in the sequence")
    print("2. Generate a list of numbers from the first to the nth")
    print("3. Exit Program")

    #Checks to make sure user input is valid
    while True:
        try:
            selection = int(input("\nType in the option number: "))
            if selection < 1 or selection > 3:
                raise ValueError #This will send it to the print message and back to the input option
            break
        except ValueError:
            print("Oops!  That was not a valid input.  Try again...")
    
    #Exits program
    if selection == 3:
        sys.exit()

    #Get the desired value of n and checks to make sure user input is valid
    while True:
        try:
            nValue = int(input("\nWhat value of n would you like to use? "))
            if nValue < 0: #or nValue > 10000:
                raise ValueError #This will send it to the print message and back to the input option
            break
        except ValueError:
            print("Oops!  That was not a valid input.  Try again...")
    
    #Does what you selected
    if selection == 1:
        print("\n" + str(calcNth(nValue)))
    if selection == 2:
        print("\n" + str(printList(nValue)))
    
    #Asks if user wants to restart program or not
    while True:
        try:
            redo = str(input("\nWould you like to restart program? (y/n): "))
            if redo == "y" or redo == "n":
                break
            raise SyntaxError #This will send it to the print message and back to the input option
        except SyntaxError:
            print("Oops!  That was not a valid input.  Try again...")
    
    #Either exits or restarts the program
    if redo == "n":
        print("\n")
        sys.exit()
    else:
        main()

if __name__ == "__main__":
	main()