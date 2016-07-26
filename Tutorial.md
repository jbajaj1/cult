# TUTORIAL #

Joshan Bajaj

William Watson

### How To Get Started ###
* Read the Wiki!
* https://wiki.acm.jhu.edu/index.php/CultProject

### First GUI ###
* Example GUI's are found in the Repository for Shirt Forms and Membership
* Templates are provided with example use of simple functions to create simple form
* Make sure to `import cult` in your python file
* `cult.createMaster(title)` -- Creates the Master Frame with the specified title
* `data = ["...", ... , "..."]` -- Create a list of the data fields you want to collect
* `cult.createLabels(data)` -- Creates all fields with entry boxes for data collection
* `cult.createButton(msg, fnc)` -- Creates a button with specified msg and executes fnc when pressed
* `cult.createLogo(imagePath)` -- Creates an image with specified file. Must be gif to work.
* `cult.creatScrollBox()` -- adds a ListBox object that can hold a list of strings
* `cult.setDimensions(H, W)` -- Sets the GUI's dimension with parameter settings
* `cult.run()` -- Executes main loop of GUI and displays GUI made with specified options.

### Email Data Collection ###
* Example Data Email Files can be found for Shirts and Membership Examples
* Setting things up is simple, just use the setters:
* `email.setFileRead(fileRead)` -- Sets input file
* `email.setFileWrite(fileWrite)` -- Sets output file
* `email.setUrl(["List of URL"])` -- Sets the URL sites to send data to
* `email.setDelim()` -- Sets the delimiter for use by program
* Now we can use the built in functions to manipulate the data:
* `email.generateEmailList()` -- Generates a text file with just emails and names
* `email.addMembers()` -- Reads the email list and submits internet forms using that info
* `email.clearFiles()` -- Clears Files
* `email.usage()` -- Prints the usage to user for supported command line arguments
* `email.removePerson(person)` -- Removes all lines that contain instance of person
* `email.run()` -- Built in cmd functionality, use is optional but provided as a convenience

### Bring It All Together ###
* We have kept our files for the gui and email services separate since it is possible that you may want to collect all of your data first than manipulate it.
* To use both modules together, just import both into your python file
* `import cult`
* `import email`
* Use the modules in the same way as described above.
* We separated them because the GYM has no internet so we would have to wait to send emails to the ACM forms.
