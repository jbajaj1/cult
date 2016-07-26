#!/usr/bin/env python
import email #import module

email.setFileRead("FILE TO READ")
email.setFileOut("OUTPUT FILE")
email.setUrl(["LISTS OF URL SITES"])


email.run() #If you want to run built in line

#If you want more control, use indivual functions already made in email with your own code.

email.generateEmailList()       #Generate Email List
email.removePerson("NAME HERE") #Remove line with param in it
email.clearInFile()             #clears input file
email.usage()                   #prints cmd line usage
email.addMembers()              #Sends data to URL sites
email.clearOutFile()            #CLears Output File
email.clearFiles()              #Clears Files
email.clearAllFiles()           #CLears All Files
