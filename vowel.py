namelst=["arun","vani","raju","raja","john","manu"]
vowlist,conlist =[],[]

vowchar = ["a", "e", "i", "o", "u"]

for name in namelst:
	if name[-1] in vowchar:
		vowlist.append(name)
	else:
		conlist.append(name)

print (vowlist)
print (conlist)



studlst = ["arun-10-20-30-40-50","ravi-45-65-34-65-45"]

name, *marks = studlst.split("-")
tot = sum(int(e) for e in marks)
print (name, tot)



1. 

arun kumar -- no delimeter split by space
f = lambda x:x.split()[0][0].upper + x.split()[1][0].upper
f = lambda x:["".join([st[0].upper() for st in x.split()])]


2. sorted(x)[-2]
max.sort(reverse=True)
max[1]

3.
sum = lambda a,b : a+b


4. 
first = lambda x: x.split("-")[0]



f = lambda x:  [st[0].upper() for st in x.split()]


