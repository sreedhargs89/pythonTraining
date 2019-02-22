class Emps:
	def __init__(self,name,dept):
		self.name = name
		self.dept = dept

	def turnupper(self):
		self.name = self.name.upper()

	def show(self):
		print ("name = %s dept = %s" %(self.name, self.dept))

		