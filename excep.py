import traceback
import sys

class ZeroError(Exception):
	def __init__(self,mesg):
		super().__init__(self)
		self.mesg = mesg

	def __str__(self):
		return self.mesg

try:
	num1 = input ("Enter ")
	num2 = input ("Enter ")
	num1 = int(num1)
	num2 = int(num2)
	if num1 == 0 or num2 == 0:
		raise ZeroError("Values cant be zero...")
	res = num1 +num2
except ValueError as e1:
	print (e1)
except ZeroError as e2:
	print (e2)
	print (type(e2))
	traceback.print_exc()
	print(sys.exc_info())
except :
	print ("What...?")
else :
	print (res)
finally:
	print ("cleanup")