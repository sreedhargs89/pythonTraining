filehandler = open("one.txt", "r")

filehandler2 = open("two.txt", "w+")
#filehandler.seek(0,1)

filehandler2.write(filehandler.read().upper())

filehandler2.seek(0,0)
print (filehandler2.read())
filehandler2.close()
filehandler.close()