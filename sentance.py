input1 = input ("Enter a number : ")

#input1 = "arvindan"
first = input1[0].upper()+input1[1:]
print (first)

sc = input1[0].upper()+input1[1:-1]+input1[-1].upper()
print (sc)


th = input1[:2].upper()+input1[2:-2]+input1[-2:].upper()
print (th)

fo = input1[:3].upper()+input1[-1:2:-1]
print (fo)
