#!/usr/bin/env python3

"""
Collatz Conjecture 
By Sean DeBarr
"""

import os
import sys
import time

def colCon(n):
    c = 0
    
    while (n > 1):
        if n % 2 == 0:
            n = n / 2
            c += 1
        else:
            n = (n * 3) + 1
            c += 1
        
    return c

def main():

    #Program starts here
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.1)
    print("\nWELCOME TO COLLATZ CONJECTURE")
    print("\nThere are two options:")
    print("1. Find the number of steps it takes to reach one given n")
    print("2. Exit Program")

    #Checks to make sure user input is valid
    while True:
        try:
            selection = int(input("\nType in the option number: "))
            if selection < 1 or selection > 2:
                raise ValueError #This will send it to the print message and back to the input option
            break
        except ValueError:
            print("Oops!  That was not a valid input.  Try again...")
    
    #Exits program
    if selection == 2:
        sys.exit()

    #Get the desired value of n and checks to make sure user input is valid
    while True:
        try:
            nValue = int(input("\nWhat value of n would you like to use? "))
            if nValue < 0:
                raise ValueError #This will send it to the print message and back to the input option
            break
        except ValueError:
            print("Oops!  That was not a valid input.  Try again...")
    
    #Does what you selected
    if selection == 1:
        print("\n" + "It takes " + str(colCon(nValue)) + " steps to reach 1.")

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