import cult

def function():
    entries = cult.getEntry(0)
    cult.deleteEntry(entries) #should delete first box only

def fnc2():
    cult.deleteEntries()

def testPopUp():
    cult.createPopUp("test", "button", 200, 200, function)
    cult.createPopUpMessage("hello msg")
    cult.displayError("Invalid Error")


cult.createMaster("Test")
data = ["Entry1", "Entry2", "Entry3"]
cult.createLabels(data) #Should see all 3 labels
cult.createLabel("Single Entry") #Should make single entry
cult.createButton("delete first box content", function)
cult.createButton("delete all boxes", fnc2)
#test pop up button
cult.createButton("pop up test", testPopUp)

entries = cult.getEntries()
if len(entries) is 4:
    print True
    
print cult.getEntryContent(0)
print cult.getFieldEntryContent("entry1")

#test List Box
cult.createScrollBox() #Should see listbox next to photo
cult.writeListBox("Joshan")
cult.writeListBox("Bill")

def sort():
    cult.sortListBox()
    
cult.createButton("sortBox", sort)

def fnc3():
    print "Radio selected"
    
MODES = [("R1", fnc3),("R2", fnc3),("R3", fnc3),("R4", fnc3),]
cult.createRadioButtons(MODES)


cult.createLogo("logo.gif") #should see photo
cult.setDimensions(700,700) #should adjust dimensions

#Run GUI
cult.run()
