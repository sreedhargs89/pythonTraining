class Stud:

	def __init__(self,name=None,marks=[0,0,0]):
	#def __init__(self,name,marks):
		self.name = name
		self.marks = marks

	def findall(self):
		self.total = sum(self.marks)
		self.avg = self.total/len(self.marks)

	def show(self):
		print("Name "+ self.name)
		print("Marks "+ str(self.marks))
		print("Total "+ str(self.total))
		print("Name "+ str(self.avg))

	def compareAvg(self, other):
		return self.total > other.total

