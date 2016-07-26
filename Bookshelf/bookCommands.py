import sys
import getopt
import os
import fileinput

string = "https://www.acm.jhu.edu/~jbajaj/ACMBookShelf/"            
home = "<a href=\"" + string + "BooksList.htm\">Back to the general library!</a>"
homeTable = "<a href=\"" + string + "Books.htm\">See table</a>"
longstring = string + "ISBNHtm/"

def removeBook(Title):
    Title += "\n"
    temp = open("temp.txt", 'w')
    bookinfo = open("bookinfo.txt", 'r')
    counter = 0
    foundTitle = 0
    removed = 0
    for line in bookinfo:
        if(foundTitle == 0):
            if(line != Title):
                temp.write(line)
            else:
                foundTitle = 1
                removed = 1
        else:
            if(counter != 16):
                if(counter == 3):
                    os.remove('./ISBNHtm/'+ line.strip('\n') + '.htm')
                counter += 1
            else:
                foundTitle = 0
                counter = 0
    temp.close()
    bookinfo.close()
    temp = open("temp.txt", 'r')
    bookinfo = open("bookinfo.txt", 'w')
    for line in temp:
        bookinfo.write(line)
    bookinfo.close()
    temp.close()
    os.remove("temp.txt")
    if(removed == 0):
        print("Title not found. Make sure you use the exact title.")


def updateOwnedCopies(Title, numCopies):
    Title += "\n"
    bookinfo = open("bookinfo.txt", 'r')
    temp = open("temp.txt", 'w')
    counter = 0
    foundTitle = 0
    changed = 0
    for line in bookinfo:
        if(foundTitle == 0):
            if(line != Title):
                temp.write(line)
            else:
                foundTitle = 1
                temp.write(line)
        else:
            if(counter != 15):
                temp.write(line)
                counter += 1
            else:
                temp.write(str(numCopies) + "\n")
                changed = 1
                foundTitle = 0
                counter = 0
    temp.close()
    bookinfo.close()
    temp = open("temp.txt", 'r')
    bookinfo = open("bookinfo.txt", 'w')
    for line in temp:
        bookinfo.write(line)
    bookinfo.close()
    temp.close()
    os.remove("temp.txt")
    if(changed == 0):
        print("Title not found. Please make sure you use the exact title.")


def updateNote(Title, Note):
    Title += "\n"
    bookinfo = open("bookinfo.txt", 'r')
    temp = open("temp.txt", 'w')
    counter = 0
    foundTitle = 0
    changed = 0
    for line in bookinfo:
        if(foundTitle == 0):
            if(line != Title):
                temp.write(line)
            else:
                foundTitle = 1
                temp.write(line)
        else:
            if(counter != 13):
                temp.write(line)
                counter += 1
            else:
                temp.write(Note + "\n")
                changed = 1
                foundTitle = 0
                counter = 0
    temp.close()
    bookinfo.close()
    temp = open("temp.txt", 'r')
    bookinfo = open("bookinfo.txt", 'w')
    for line in temp:
        bookinfo.write(line)
    bookinfo.close()
    temp.close()
    os.remove("temp.txt")
    if(changed == 0):
        print("Title not found. Please make sure you use the exact title.")

def updateRec(Title, RecommendedFor):
    Title += "\n"
    bookinfo = open("bookinfo.txt", 'r')
    temp = open("temp.txt", 'w')
    counter = 0
    foundTitle = 0
    changed = 0
    for line in bookinfo:
        if(foundTitle == 0):
            if(line != Title):
                temp.write(line)
            else:
                foundTitle = 1
                temp.write(line)
        else:
            if(counter != 14):
                temp.write(line)
                counter += 1
            else:
                temp.write(RecommendedFor + "\n")
                changed = 1
                foundTitle = 0
                counter = 0
    temp.close()
    bookinfo.close()
    temp = open("temp.txt", 'r')
    bookinfo = open("bookinfo.txt", 'w')
    for line in temp:
        bookinfo.write(line)
    bookinfo.close()
    temp.close()
    os.remove("temp.txt")
    if(changed == 0):
        print("Title not found. Please make sure you use the exact title.")


def updateRating(Title, Rating):
    Title += "\n"
    bookinfo = open("bookinfo.txt", 'r')
    temp = open("temp.txt", 'w')
    counter = 0
    foundTitle = 0
    changed = 0
    for line in bookinfo:
        if(foundTitle == 0):
            if(line != Title):
                temp.write(line)
            else:
                foundTitle = 1
                temp.write(line)
        else:
            if(counter != 5):
                temp.write(line)
                counter += 1
            else:
                temp.write(str(Rating) + "\n")
                changed = 1
                foundTitle = 0
                counter = 0
    temp.close()
    bookinfo.close()
    temp = open("temp.txt", 'r')
    bookinfo = open("bookinfo.txt", 'w')
    for line in temp:
        bookinfo.write(line)
    bookinfo.close()
    temp.close()
    os.remove("temp.txt")
    if(changed == 0):
        print("Title not found. Please make sure you use the exact title.")


def clearBooks():
    #Clears BooksList.htm and Books.htm of all books. Useful for testing.
    lst = open("BooksList.htm", 'w')
    lst.write("<head>\n<link rel = \"stylesheet\" href=\"test.css\"></link>\n</head>\n<a href=\"https://www.acm.jhu.edu/~jbajaj/ACMBookShelf/Books.htm\">See Table</a>\n<ul>\n</ul>")
    lst.close()
    tbl = open("Books.htm", 'w')
    tbl.write("<head>\n<link rel = \"stylesheet\" href = \"test.css\"></link>\n</head>\n<a href=\"https://www.acm.jhu.edu/~jbajaj/ACMBookShelf/BooksList.htm\">See List</a>\n<table class=\"table table-bordered table-hover table-condensed\">\n<tbody><tr>\n<th>Title</th>\n<th>Author</th>\n<th>Author l-f</th>\n<th>Additional Authors</th>\n<th>ISBN</th>\n<th>ISBN13</th>\n<th>ACM Rating</th>\n<th>Average Rating</th>\n<th>Publisher</th>\n<th>Binding</th>\n<th>Number of Pages</th>\n<th>Year Published</th>\n<th>Original Publication Year</th>\n<th>Date Added</th>\n<th>Private Notes</th>\n<th>Recommended For</th>\n<th>Owned Copies</th>\n</tr>\n</tbody></table>")
    tbl.close()


def sortBookInfo():
    #Sorts BookInfo file
    bookinfo = open("bookinfo.txt", 'r')
    temp = open("temp.txt", 'w')
    temp2 = open("temp2.txt", 'w')
    count = 0
    for line in bookinfo:
        if (count == 0):
            temp.write(line)
            count = count + 1
        else:
            count = count + 1
        if (count == 18):
            count = 0
    bookinfo.close()
    bookinfo = open("bookinfo.txt", 'r')
    for line in bookinfo:
        temp2.write(line)
    bookinfo.close()
    temp2.close()
    os.remove("bookinfo.txt")
    temp.close()
    temp = open("temp.txt", 'r')
    sortedTitles = temp.readlines()
    sortedTitles = sorted(sortedTitles, key=lambda s: s.lower())
    temp.close()
    os.remove("temp.txt")
    temp = open("temp.txt", 'w')
    for title in sortedTitles:
        temp.write(title)
    temp.close()
    temp = open("temp.txt", 'r')
    bookinfo = open("bookinfo.txt", 'w')
    for title in temp:
        temp2 = open("temp2.txt", 'r')
        for line in temp2:
            if(title == line):
                bookinfo.write(line)
                counter = 0
                while(counter != 17):
                    bookinfo.write(next(temp2))
                    counter = counter + 1
                temp2.close()
                break
    bookinfo.close()
    temp.close()
    temp2.close()
    os.remove("temp.txt")
    os.remove("temp2.txt")

    
def usage():
    print "To Sort Book File:"
    print "\tpython bookCommands.py -s"
    print "To Remove a Book:"
    print "\tpython bookCommands.py -r \"book to remove\""
    print "To add File content to Books:"
    print "\tpython bookCommands.py -a \"filename\""
    print "To clear content of Books files:"
    print "\tpython bookCommands.py -c"
    print "To update the number of owned copies of a book:"
    print "\tpython bookCommands.py -o \"TITLE|||NUMBER\""
    print "To update the notes of a book:"
    print "\tpython bookCommands.py -o \"TITLE|||NOTE\""
    print "To update the reccommended for section of a book:"
    print "\tpython bookCommands.py -o \"TITLE|||REC\""
    print "To update the my rating column for a book:"
    print "\tpython bookCommands.py -o \"TITLE|||RATE\""

def addToTable(book):
    #adds to Books
    a = open("Books.htm", 'r')
    content = ""
    for line in a:
        if "</tbody></table>" not in line:
            content += line
        else:
            content += printHTMLTable(book) + "\n" + line
    a.close()
    ar = open("Books.htm" , 'w')
    ar.write(content)
    ar.close()

def addToList(book):
    #adds to list file
    r = open("BooksList.htm", 'r')
    content = ""
    for line in r:
        if line != "</ul>":
            content += line
        else:
            content += printList(book) + "\n" + line
    r.close()
    
    f = open("BooksList.htm", 'w')
    f.write(content)
    #f.write(home + "\n" + homeTable)
    f.close()


def addISBNfile(book):
    #makes separate table file
    string = "ISBNHtm/" + str(book[4])
    url = string[:-1] + ".htm"
    w = open(url, 'w')
    w.write("<head><link rel=\"stylesheet\" href=\"test.css\"></link></head>\n")
    w.write("<table class=\"table table-bordered table-hover table-condensed\"><tbody>\n")
    w.write(printHTML(["Title", "Author", "Author l-f", "Additonal Authors", "ISBN", "ISBN13", "ACM Rating", "Average Rating", "Publisher", "Binding", "Number of Pages", "Year Published", "Original Publication Year", "Date Added", "Private Notes", "Recommended For", "Owned Copies"]))
    w.write(printHTML(book))
    w.write("</tbody></table>")
    w.write(home)
    w.write(homeTable)
    w.close()

    
def printList(book):
    global string
    global longstring
    url = longstring + str(book[4]) + ".htm"
    line = "<li><a href=\"" + url + "\">" + str(book[0]) + " -- " + str(book[1]) + "</a></li>"
    return line
    
def printHTML(book):
    line = "<tr>"
    count = 0
    for item in book:
      if count != 17:
         line += "<td>" + str(item) + "</td>\n"
         count = count + 1
    line += "</tr>\n"
    return line

def printHTMLTable(book):
    global longstring
    line = "<tr>"
    count = 0
    for item in book:
        if count == 0:
            url = longstring + str(book[4]) + ".htm"
            line += "<td>" + "<a href=\"" + url + "\">" + str(item) + "</a></td>"
        elif count != 17:
            line += "<td>" + str(item) + "</td>\n"
        count = count + 1
    line += "</tr>\n"
    return line


def addFileBooks(filename):
    f = open(filename, 'r')
    book = []
    count = 0
    for line in f:
        if(count < 17):
            book.append(line)
            count = count + 1
        elif(count == 17):
            empty =""
            url = str(book[4]) + ".htm"
            ISBN = book[4]
            addToTable(book)
            addToList(book)
            addISBNfile(book)
            count = 0
            book = []
    f.close()

argv = sys.argv[1:]
try:
    opts, args = getopt.getopt(argv, "hr:sa:c", ["help"])
except getopt.GetoptError:
    usage()
    sys.exit(2)

argv = sys.argv[1:]
try:
    opts, args = getopt.getopt(argv, "hsr:a:co:n:e:m:", ["help"])
except getopt.GetoptError:
    usage()
    sys.exit(2)

for opt,arg in opts:
    if opt in ("-h", "-help"):
        usage()
        sys.exit()
    elif opt in '-s':
        sortBookInfo()
    elif opt in '-r':
        removeBook(arg)
    elif opt in '-a':
        addFileBooks(arg)
    elif opt in '-c':
        clearBooks()
    elif opt in '-o':
        lst = arg.split("|||")
        updateOwnedCopies(lst[0], lst[1])
    elif opt in '-n':
        lst = arg.split("|||")
        updateNote(lst[0], lst[1])
    elif opt in '-e':
        lst = arg.split("|||")
        updateRec(lst[0], lst[1])
    elif opt in '-m':
        lst = arg.split("|||")
        updateRating(lst[0], lst[1])