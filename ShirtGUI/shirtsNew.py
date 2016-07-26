#!/user/bin/env python
import cult


def addMember():
    entry = cult.getEntries()
    if cult.validateEmail(entry[1].get()):
        cult.writeData("shirts.txt")
    else:
        cult.displayError("Invalid Email")
    cult.deleteEntries()

cult.createMaster("Shirt Order Form")
fields = ["Name", "Email", "Shirt Size"]
cult.createLabels(fields)
cult.createButton("ADD", addMember)
cult.createLogo("logo.gif")
cult.run()
