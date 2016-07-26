import email

email.setFileRead("testFile.txt")
email.setFileWrite("testOut.txt")

email.generateEmailList()

email.setFileWrite("testRemove.txt")
email.removePerson("test")

email.setFileWrite("clearTest.txt")
f = open("clearTest.txt" , 'w')
for i in range(0,100):
    f.write(str(i) + "\n")
f.close()

email.clearOutFile()

email.setFileWrite("sortTest.txt")
f = open("sortTest.txt", 'w')
f.write("Zaul")
f.write("Xaul")
f.write("Yul")
f.write("Maul")
f.write("Naul")
f.write("Eaul")
f.write("Daul")
f.write("Caul")
f.write("Baul")
f.write("Aaul")
f.close()

email.sortFile("sortTest.txt")

email.usage()

print "All Tests pass"
