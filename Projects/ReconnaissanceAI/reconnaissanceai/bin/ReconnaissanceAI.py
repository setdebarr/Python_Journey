#!/usr/bin/env python3.7

import nmap
import pyttsx3
import os

engine = pyttsx3.init()
engine.say("Executing Startup")

def main():
    engine.say("Please enter target ip")
    engine.runAndWait()
    targetIP = input("IP: ")

    engine.say("Would you like to specify a port range")
    engine.runAndWait()
    portrangeQ = input("y/n: ")
    if portrangeQ == "y":
        engine.say("Please enter port range")
        engine.runAndWait()
        portrange = input("#-#: ")


    nm = nmap.PortScanner()
    if portrangeQ == "y":
        engine.say("Scanning" + str(targetIP) + "Range" + str(portrange))
        engine.runAndWait()
        #os.system("nmap " + str(targetIP) + " -p" +str(portrange) + " -vv -sV")
        nm.scan(hosts=targetIP, ports=portrange)
        print(nm.scaninfo())
    else:
        engine.say("Scanning" + str(targetIP))
        engine.runAndWait()
        #os.system("nmap " + str(targetIP) + " -vv -sV")
        nm.scan(hosts=targetIP)
        print(nm.scaninfo())

if __name__ == "__main__":
	main()

# engine.runAndWait() 
# engine.say("")