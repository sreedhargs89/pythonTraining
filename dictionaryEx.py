
dept = {
	101 : "sales",
	102 : "purch",
	103 : "accts",
}

emps ={
	"arun" : "blr-IMS-101",
	"john" : "chn-ST0-103"
}


#inp = input ("Enter the Name :")
inp = "arun"


if inp in emps:
	print ("Name = "+inp)
	print ("loc = "+emps[inp].split("-")[0])
	print ("pro = "+emps[inp].split("-")[1])
	print ("dept = "+dept[int(emps[inp].split("-")[2])])



alpha =["a", "b", "c", "d", "e"]
nums = [1,2,3,4,5]
print(zip(alpha,nums))


#way1:
for key,value in zip(alpha,nums):
	res[key] = value
#way2:
res = {key:value for key,value in zip (ala, nums)}
#way3:
res=dict(zip(alpha,nums))

print (res)



