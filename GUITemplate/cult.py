#!/usr/bin/env python
from Tkinter import *
import re
"""
use chmod +x cult.py
"""

"""
Global Variables
"""
master = Tk()
entries = []
fields =[]
rowNum = 0
scrollbar = Scrollbar(master)
listbox = Listbox(master, yscrollcommand = scrollbar.set)
logo = Label()
logoRow = 0

"""
METHODS FOR CULT
"""

"""
Creates a more specific PopUp Widget with custom message and button
"""
def createPopUp(message, buttonMessage, width, height, cmd):
   toplevel = Toplevel()
   toplevel.geometry(str(width) + "x" + str(height))
   Label(toplevel, text=message).pack(side=TOP)
   Button(toplevel, text=buttonMessage, command=cmd).pack(side=BOTTOM)
   Button(toplevel, text="OK", command = toplevel.destroy).pack(side=BOTTOM)
   

"""
Create a Pop-Up Widget with a message
"""
def createPopUpMessage(message):
   toplevel = Toplevel()
   toplevel.geometry("200x75")
   Label(toplevel, text=message).pack(side=TOP)
   Button(toplevel, text="OK", command=toplevel.destroy).pack(side=BOTTOM)
   
   
"""
Create an adjustable size Pop-Up Widget with a message
"""
def createPopUpAdjMessage(message, width, height):
   toplevel = Toplevel()
   toplevel.geometry(str(width) + "x" + str(height))
   Label(toplevel, text=message).pack(side=TOP)
   Button(toplevel, text="OK", command = toplevel.destroy).pack(side=BOTTOM)


"""
Displays custom error message pop up window
"""
def displayError(error):
   toplevel = Toplevel()
   toplevel.geometry("200x75")
   Label(toplevel, text=error).pack(side=TOP)
   Button(toplevel, text="OK", command=toplevel.destroy).pack(side=BOTTOM)
   
"""
Delete text in all entries
"""
def deleteEntries():
   for entry in entries:
      entry.delete(0, END)

"""
Delete text in particular entry
"""
def deleteEntry(entry):
   entry.delete(0, END)
      
"""
Returns list of entries objects
"""
def getEntries():
   return entries

"""
Returns list of content from Entry Boxes
"""
def getEntriesContent():
   lst = []
   for entry in entries:
      lst.append(entry.get())
   return lst

"""
Returns entry object at given index
"""
def getEntry(index):
   return entries[index]

"""
Returns Dictionary of Fields to Entry Boxes
"""
def getFieldEntry():
   return dict(zip(fields, entries))

"""
Returns dictionary of Fields and Entry COntent
"""
def getFieldEntryContent():
   return dict(zip(fields, getEntriesContent()))

"""
Returns contents of entry box
"""
def getEntryContent(index):
   return entries[index].get()

"""
Returns the content of entry box given a field
"""
def getFieldEntryContent(field):
   field.lower()
   item = findEntry(field)
   if item is None:
      return ""
   return item.get()
   
"""
Returns the list of names of fields
"""
def getFields():
   return fields

"""
Returns the name of the field at a given index
"""
def getField(index):
   return fields[index]

"""
Returns index of  a field
"""
def findField(field):
   field = field.lower()
   count = 0
   for name in fields:
      if name == field:
         return count
      count = count + 1
   return -1

"""
Returns entry for a field
"""
def findEntry(field):
   field = field.lower()
   count = 0
   for name in fields:
      if name == field:
         return entries[count]
      count = count + 1
   return None

"""
Write to ListBox
"""
def writeListBox(name):
   listbox.insert(END, name)
   
"""
Writes all data entries to file, separated by '|'
"""
def writeData(filename):
   f = open(filename, 'a')
   line = ""
   for i in range(0, len(entries)):
      line += entries[i].get()
      if i+1 is not len(entries):
         line += "|"
   line += "\n"
   f.write(line)
   f.close()

"""
Writes data to file using given dilimiter
"""
def writeDataDelim(filename, delim):
   f = open(filename, 'a')
   line = ""
   for i in range(0, len(entries)):
      line += entries[i].get()
      if i+1 is not len(entries):
         line += delim
   line += "\n"
   f.write(line)
   f.close()

"""
Validate Email
"""
def validateEmail(email):
   if re.match(r"(^[a-zA-Z0-9_.+-}+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
      return True
   return False

"""
Find the index of the email entry field
"""
def findEmailIndex():
   count = 0
   for name in fields:
      if name.lower() == "email":
         return count
      count = count + 1
   return -1;

"""
Creates the Master Frame for the GUI
"""
def createMaster(title):
   master.title(title)
   master.geometry("515x620")
   
   
"""
Creates all data fields for GUI
"""
def createLabels(textFields):
   global rowNum
   for name in textFields:
      fields.append(name)
      Label(master, text=name).grid(row = rowNum, sticky=E)
      e = Entry(master)
      e.grid(row = rowNum, column=1, sticky=W)
      rowNum=rowNum+1
      entries.append(e)


"""
Creates a Label without Entry Box
"""
def createTextLabel(msg):
   global rowNum
   Label(master, text=msg).grid(row=rowNum, columnspan=2)
   rowNum=rowNum+1

"""
Creates a single data field for GUI
"""
def createLabel(name):
   global rowNum
   fields.append(name)
   Label(master, text=name).grid(row = rowNum, sticky=E)
   e = Entry(master)
   e.grid(row = rowNum, column=1, sticky=W)
   rowNum=rowNum+1
   entries.append(e)
    

"""
Creates a button
"""
def createButton(name, cmd):
   global rowNum
   Button(master, text=name, command=cmd).grid(row = rowNum, columnspan=3)
   rowNum=rowNum+1

"""
Creates a Set of Radio Buttons
MODES is a Dictionary of text to functions
Each value is distinct
"""
def createRadioButtons(MODES):
   global rowNum
   v = StringVar()
   v.set("L")
   count = 0
   for text, cmd in MODES:
      b = Radiobutton(master, command=cmd, indicatoron=0, text=text, variable=v, value=count)
      b.grid(row = rowNum, columnspan = 2)
      rowNum = rowNum + 1
      count = count + 1

   
"""
Sets geometry of the master frame
"""
def setDimensions(width, height):
   master.geometry(str(width) + "x" + str(height))
   

"""
Sets the title of the master frame
"""
def setTitle(title):
   master.title(title)


"""
Creates the Master Frame for the GUI with adjustable dimensions.
"""
def createMasterAdj(title, width, height):
   master.title(title)
   master.geometry(str(width) + "x" + str(height))

   
"""
Logo Creation
"""
def createLogo(fileName):
   global rowNum
   global logo
   global logoRow
   photo = PhotoImage(file=fileName)
   logo = Label(master, image=photo)
   logo.image = photo
   logo.grid(row = rowNum, column = 0, columnspan=2, rowspan=20, sticky=W+E+N+S, padx=5, pady=5)
   logoRow=rowNum
   rowNum=rowNum+1
   
   
"""
The Scrollbar and Listbox
"""
def createScrollBox():
   global scrollbar
   global listbox
   global logoRow
   scrollbar = Scrollbar(master)
   scrollbar.grid(row=logoRow, column=4, columnspan=1, rowspan=20)
   listbox = Listbox(master, yscrollcommand = scrollbar.set)
   listbox.grid(row=logoRow, column=3, columnspan=1, rowspan=20)
   listbox.config()
   scrollbar.config(command = listbox.yview)

"""
Sorts the items in ListBox
"""
def sortListBox():
   global listbox
   names = getListBoxItems()
   lst = list(names)
   lst = mergeSort(lst)
   listbox.delete(0, END)
   for item in lst:
      listbox.insert(END, item)

"""
Sorts the input list using the merge sort algorithm.
"""
def mergeSort(items):
   if len(items) > 1:
      mid = len(items) // 2        # Determine the midpoint and split
      left = items[0:mid]
      right = items[mid:]
      mergeSort(left)            # Sort left list in-place
      mergeSort(right)           # Sort right list in-place
      l, r = 0, 0
      for i in range(len(items)):     # Merging the left and right list
         lval = left[l] if l < len(left) else None
         rval = right[r] if r < len(right) else None
         if (lval is not None and rval is not None and lval < rval) or rval is None:
            items[i] = lval
            l += 1
         elif (lval is not None and rval is not None and lval >= rval) or lval is None:
            items[i] = rval
            r += 1
         else:
            raise Exception('Could not merge, sub arrays sizes do not match the main array')
   return items

"""
Deletes All Items in ListBox
"""
def deleteListBoxItems():
   global listbox
   listbox.delete(0, END)
   
   
"""
Deletes the oldest item in ListBox
"""
def deleteLastListBoxItem():
   global listbox
   listbox.delete(END)
   

"""
Returns item at listbox index
"""
def getItemListBox(index):
   global listbox
   return listbox.get(index)

"""
Returns all items in ListBox
"""
def getListBoxItems():
   global listbox
   return listbox.get(0, END)
   
"""
Runs Main Loop of GUI
"""
def run():
   mainloop()
