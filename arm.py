###################################################################
## Exercise to find the given/input number is armstrong of not
## Logic: An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371.
###################################################################
inp = input ("Enter a number/string : ")
#inp = "371"

length = len(inp)
print (length)

tot=0

for e in inp:
	tot = tot+int(e)**length

print (tot)

if tot == int(inp):
	print ("This is an Armstrong number")
else:
	print ("This is not an Armstrong number")