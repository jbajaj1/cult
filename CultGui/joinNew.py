#!/usr/bin/env python
import cult

"""
addMember()
-custom method for join.py
maybe should be in different file, like join.py
"""
def addMember():
    index = cult.findEmailIndex() #Actually don't need this
    #if index is -1: return
    entry = cult.getEntries()
    email = entry[index].get() #User should know index of email anyway.
    if cult.validateEmail(email):
        cult.writeData("file.txt")
        cult.writeListBox(entry[0].get())
    else:
        cult.displayError("Invalid Email")
    cult.deleteEntries()
    
"""
If cult.py works, this is all one needs to replicate join.py
"""
cult.createMaster("Join ACM!")
data = ["Name", "Email", "Year"]
cult.createLabels(data)
cult.createButton("JOIN!", addMember)
cult.createLogo("logo.gif")
cult.createScrollBox()
cult.setDimensions(700, 700)
cult.run()
