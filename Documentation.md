# DOCUMENTATION GUIDE #

### Contributors ###

* Joshan Bajaj
* William Watson

### Step 1: GUI Creation ###
* `cult.py` contains all necessary functions to create a simple gui to collect user information
* `import cult` should be used in the `[GuiNameHere].py` file to access the module's functions, and functions should be called as such: `cult.function(parameters)`
* When information is done being collected, simply close out of the GUI
* Internet access not needed

### Step 2: Adding to MailLists ###

* If you would like to generate the email list, type `python email.py -g`
* If you would like to delete the file containing the newly obtained emails, type `python email.py -c`
* If you would like to add the emails from the email list to the acm mailing lists, type `python email.py -j`
* If you would like to delete a specific person from the email list, type `python email.py -r 'NAMEHERE'`
* Feel free to mix and match the flags, order matters. Generally, `-g -j -c` would be the most logical order
* Internet access needed

### Function Documentation ###
* For in-depth documentation on the functions in email.py, visit https://wiki.acm.jhu.edu/index.php/CultProject#Functions_-_email.py
* For in-depth documentation on the functions in cult.py, visit https://wiki.acm.jhu.edu/index.php/CultProject#Functions_-_cult.py
