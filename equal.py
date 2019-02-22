import math
#input1 = input ("Enter the sentance : ")

input1 ="this is the This"
flst = input1.split()

#print (flst[0])
#print (flst[-1])

if (flst[0].lower() == flst[-1].lower()):
    print ("Equal")
else:
    print ("Not equal")



str1= "arun-10,20,30,40,50,60"
str2="ravi-40,50,60,70,10,25"


aflst=str1.split("-")[1].split(",")
rflst=str1.split("-")[1].split(",")


r1 = sum([int(i) for i in aflst])
r2 = sum([int(i) for i in rflst])

if r1 > r2:
    print ("arun is best")
else:
    print ("ravi is best")




a = "10-63-81-17"
s= a.split("-")
r= "-".join([str(int(i)+1) for i in s])
#k= [str(i) for i in r]
#b ="-".join(r)

print (r)
