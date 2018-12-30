#!/usr/bin/env python3

import nmap
import os
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Executing Startup")
print("\nExecuting Startup" + "\n")

def main():
    engine.say("Please enter target ip")
    print("Please enter target ip")
    engine.runAndWait()
    targetIP = input("IP: ")

    engine.say("Would you like to specify a port range")
    print("\nWould you like to specify a port range")
    engine.runAndWait()
    portrangeQ = input("y/n: ")
    if portrangeQ == "y":
        engine.say("Please enter port range")
        print("\nPlease enter port range")
        engine.runAndWait()
        portrange = input("#-#: ")


    nm = nmap.PortScanner()
    if portrangeQ == "y":
        engine.say("Scanning" + str(targetIP) + "Range" + str(portrange))
        print("\nScanning " + str(targetIP) + " Range " + str(portrange) + "\n")
        engine.runAndWait()
        #os.system("nmap " + str(targetIP) + " -p" +str(portrange) + " -vv -sV")
        nm.scan(hosts=targetIP, ports=portrange, arguments="-sV")
        print(nm.scaninfo())
    else:
        engine.say("Scanning" + str(targetIP))
        print("\nScanning " + str(targetIP) + "\n")
        engine.runAndWait()
        #os.system("nmap " + str(targetIP) + " -vv -sV")
        nm.scan(hosts=targetIP, arguments="-sV")
        print(nm.scaninfo)

if __name__ == "__main__":
	main()

# engine.runAndWait() 
# engine.say("")