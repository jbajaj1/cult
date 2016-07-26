#!/usr/bin/env python
import sys
import getopt
import urllib
import urllib2
from tempfile import mkstemp
from shutil import move
from os import remove, close

"""
Global
"""
fileRead = ""
fileOut = ""
urlSites = []
delim = "|"

"""
METHODS FOR EMAIL
"""

"""
Sets the url sites to send to
"""
def setUrl(urlNames):
   global urlSites
   for site in urlNames:
      urlSites.append(site)
"""
Sets Delimiter for file reading and wrtiting
"""
def setDelim(newDelim):
   global delim
   delim = newDelim

"""
Sets file that is read in
"""
def setFileRead(fileName):
   global fileRead
   fileRead = fileName

"""
Sets File to Write to
"""   
def setFileWrite(fileName):
   global fileOut
   fileOut = fileName

"""
Generate the Email List from files
Assumes Email is second item in line
"""
def generateEmailList():
   global fileOut
   global fileRead
   global delim
   w = open(fileOut, 'a')
   f = open(fileRead, 'r')
   while True:
      line = f.readline()
      if not line: break
      indexer = line.split(delim)
      w.write(indexer[1] + "\n")
   f.close()
   w.close()
   print "Generating email list..."


"""
Removes a Person from a file list
"""
def removePerson(person):
   global fileOut
   fh, abs_path = mkstemp()
   count = 0
   with open(abs_path, 'w') as new_file:
      with open(fileOut) as old_file:
         for line in old_file:
            if person in line:
               new_file.write(line.replace(line,""))
               count=count+1
            else:
               new_file.write(line)
   close(fh)
   remove(fileOut)           
   move(abs_path, fileOut)   
   print "Removing " + person + " from list..."
   if count is 0:
      print "Could not find " + person + " in list..."
   else:
      print "Deleted " + str(count) + " instances of " + person + " from list..."

"""
Sends Information to Forms
"""      
def addMembers():
   global fileRead
   #Can use urlSites now
   #url_1 = 'https://lists.acm.jhu.edu/mailman/subscribe/acm'
   #url_2 = 'https://lists.acm.jhu.edu/mailman/subscribe/announce'
   with open(fileRead, 'r') as f:
      for line in f:
         index = line.find(delim)
         fullname = line[:index]
         email = line[index+1:len(line)-1]
         payload = {'email' : email, 'fullname' : fullname}
         data = urllib.urlencode(payload)
         for site in urlSites:
            urllib.urlopen(site, data)
         #results1 = urllib.urlopen(url_1, data)
         #results2 = urllib.urlopen(url_2, data)
   print "Adding members..."

"""
Clears Files being worked on
"""   
def clearFiles():
   global fileOut
   #f = open('cult.txt', 'w')
   #Should we delete email_list, maybe only cult?
   a = open(fileOut, 'w')
   a.close()
   print "All contents of "+fileOut+" deleted..."

"""
Clears out file
"""
def clearOutFile():
   global fileOut
   a = open(fileOut, 'w')
   a.close()
   print "All contents of " + fileOut+" deleted..."

"""
Clears in file
"""
def clearInFile():
   global fileIn
   a = open(fileIn, 'w')
   a.close()
   print "All contents of "+ fileIn+ " deleted..."

"""
Clears all Files
"""
def clearAllFiles():
   clearOutFile()
   clearInFile()

"""
Sorts the contents of a file, via MergeSort
"""
def sortFile(filename):
   f = open(filename, 'r')
   data = []
   for line in f:
      data.append(line)
   f.close()
   data = mergeSort(data)
   f = open(filename, 'w')
   for line in data:
      f.write(line)
   f.close()
   print "Sorted data within " + filename + " via MergeSort..."
   
"""
Sorts the input list using the merge sort algorithm.
"""
def mergeSort(lst):
   if len(lst) <= 1:
      return lst
   mid = len(lst) / 2
   left = mergeSort(lst[:mid])
   right = mergeSort(lst[mid:])
   return merge(left, right)

"""
Takes two sorted lists and returns a single sorted 
list by comparing the elements one at a time.
"""
def merge(left, right):
   if not left:
      return right
   if not right:
      return left
   if left[0] < right[0]:
      return [left[0]] + merge(left[1:], right)
   return [right[0]] + merge(left, right[1:])


"""
Declares usage for script
"""
def usage():
   print "Suggested runtime configuration:"
   print "\tpython email.py -g -a -c"
   print "For help:"
   print "\tpython email.py -{h/help}"
   print "To add members:"
   print "\tpython email.py -a"
   print "To clear file:"
   print "\tpython email.py -c"
   print "To generate email list:"
   print "\tpython email.py -g"
   print "To remove a person:"
   print "\tpython email.py -r 'person to remove'"
   print ""

   
"""
Command Line Run, Built in use
"""
def run():
   global fileRead
   global fileOut
   if fileRead == "":
      fileRead = "cult.txt"
   if fileOut == "":
      fileOut = "email_list.txt"  
   argv = sys.argv[1:]
   try:
      opts, args = getopt.getopt(argv, "hdgr:a", ["help"])
   except getopt.GetoptError:
      usage()
      sys.exit(2)
   for opt,arg in opts:
      if opt in ("-h", "-help"):
         usage()
         sys.exit()
      elif opt in '-d':
         clearFiles()
      elif opt in '-g':
         generateEmailList()
      elif opt in '-r':
         removePerson(arg)
      elif opt in '-a':
         addMembers()
      
