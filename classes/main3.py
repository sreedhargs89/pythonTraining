import Stud

st1 = Stud.Stud("hari", [10,20,30,40])
print (st1.name)

st2 = Stud.Stud(marks=[30,40,50,60],name="ravi")
print (st2.name)


st1.findall()
st1.show()
st2.findall()
st2.show()

st3 = Stud.Stud()

if st1.compareAvg(st2):
	print (st1.name +" is better than "+ st2.name)
else:
	print (st2.name + " is better than "+ st1.name)