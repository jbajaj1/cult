#!/usr/bin/env python
import cult #imports the module

"""
Template File Used to Help Create Quick GUI
"""


"""
Dummy Function for Template Use Only
"""
def function():
    return 0

cult.createMaster("ADD TITLE HERE")
data = ["ADD", "FIELDS", "HERE"]
cult.createLabels(data)
cult.createButton("ADD BUTTON MESSAGE HERE", function)
cult.createLogo("logo.gif") #replace with photo file path
cult.createScrollBox()
cult.setDimensions(700,700)
cult.run()
