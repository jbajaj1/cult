import cult
import os
import webbrowser

def addBook():
    global labels
    global string
    global home
    global homeTable
    global longstring
    entries = cult.getEntries()
    book = []
    for entry in entries:
        book.append(entry.get())
    cult.deleteEntries()

    url = str(book[4]) + ".htm"
    ISBN = book[4]
    addToTable(book)
    addToList(book)
    addISBNfile(book)
    addToBookinfo(book)
    

def addToBookinfo(book):
    #adds to bookinfo.txt
    a = open("bookinfo.txt", 'a')
    count = 0
    for line in book:
        a.write(line)
        if(count != 18):
            a.write("\n")
            count += 1
    a.close()

def addToTable(book):
    #adds to Books
    a = open("Books.htm", 'r')
    content = ""
    for line in a:
        if "</tbody></table>" not in line:
            content += line
        else:
            content += printHTML(book) + "\n" + line
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
    url = "ISBNHtm/" + str(book[4]) + ".htm"
    w = open(url, 'w')
    w.write("<head><link rel=\"stylesheet\" href=\"test.css\"></link></head>\n")
    w.write("<table class=\"table table-bordered table-hover table-condensed\"><tbody>\n")
    w.write(printHTML(cult.getFields()))
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
                                                            
def printHTML(book):
    line = "<tr>"
    count = 0
    for item in book:
        if count != 17:
            line += "<td>" + str(item) + "</td>\n"
        count = count + 1
    line += "</tr>\n"
    return line
                            

def search():
    ISBN = cult.getEntry(17).get()
    #cult.deleteEntries()
    cult.deleteEntry(17)
    url = "https://www.goodreads.com/book/isbn/" + str(ISBN)
    webbrowser.open(url, new = 1)

#def addBooksFile():
#    filename = cult.getEntry(18).get()
#    cult.createPopUpMessage(filename)
    
string = "https://www.acm.jhu.edu/~jbajaj/ACMBookShelf/"            
home = "<a href=\"" + string + "BooksList.htm\">Back to the general library!</a>"
homeTable = "<a href=\"" + string + "Books.htm\">See table</a>"
longstring = string + "ISBNHtm/"


#GUI Code
cult.createMaster("Bookshelf")

labels = ["Title", "Author", "Author l-f", "Additonal Authors", "ISBN", "ISBN13", "ACM Rating", "Average Rating", "Publisher", "Binding", "Number of Pages", "Year Published", "Original Publication Year", "Date Added", "Private Notes", "Recommended For", "Owned Copies"]


cult.createPopUpMessage("Please fill out as much\n of the information as you\n can before adding a book!")
cult.createPopUpAdjMessage("If you don't know all of the\ninformation, use the\nISBN search button.\n(Internet Required)", 250, 100)
cult.createTextLabel("Add Book to Library")
cult.createLabels(labels)
cult.createButton("Add Book to Library", addBook)
cult.createTextLabel("")
cult.createTextLabel("Search For Book By ISBN Number")
cult.createLabel("ISBN or ISBN13")
cult.createButton("Search", search)
#cult.createTextLabel("")
#cult.createLabel("File Name:")
#cult.createButton("Feed in File", addBooksFile)
cult.createLogo("./book.gif")
cult.setDimensions(430, 860)
webbrowser.open("https://www.acm.jhu.edu/~jbajaj/ACMBookShelf/Books.htm", new=1)


cult.run()
