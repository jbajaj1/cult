#!/usr/bin/env python
from Tkinter import *
import re
#use chmod +x shirts.py
count = 0;

def addMember():
    #Change Regex
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", e2.get()):
        f = open('shirts.txt', 'a')
        line = e1.get() + "|" + e2.get() + "|" + e3.get().upper() + "\n"
        f.write(line)
        f.close()
        #person = e1.get()
        #global count
        #mod = count / 19
        #Change to scroll bar
        #listbox.insert(END, person)
        #listbox.grid()
        #Label(master, text=person).grid(row=count % 19 + 5, column=mod+3)
        #count = count + 1
    else:
        toplevel = Toplevel()
        toplevel.geometry("200x75")
        Label(toplevel, text="Invalid Email").pack(side=TOP)
        Button(toplevel, text="OK", command=toplevel.destroy).pack(side=BOTTOM)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
        
        
        
master = Tk()
master.title("Shirt Order Form")
master.geometry("515x620")
Label(master, text="Name:").grid(row=0, sticky=E)
Label(master, text="Email:").grid(row=1, sticky=E)
Label(master, text="Shirt Size:").grid(row=2, sticky=E)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=0, column=1, sticky=W)
e2.grid(row=1, column=1, sticky=W)
e3.grid(row=2, column=1, sticky=W)

Button(master, text="Add", command=addMember).grid(row=3, columnspan=3)
logo = PhotoImage(file="./logo.gif")
Label(master, image=logo).grid(row = 4, column = 0, columnspan=2, rowspan=20, sticky=W+E+N+S, padx=5, pady=5)
#Label(master, text="People who have already joined: ").grid(row=4, column=3, columnspan=3)
#scrollbar = Scrollbar(master)
#scrollbar.grid(row=4, column=4, columnspan=1, rowspan=20)
#listbox = Listbox(master, yscrollcommand = scrollbar.set)
#listbox.grid(row=4, column=3, columnspan=1, rowspan=20)
#listbox.config()
#scrollbar.config(command = listbox.yview)

mainloop()
