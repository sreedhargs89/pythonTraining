import Emps
import os.path

e1 = Emps.Emps("arun", "sales")
print(vars(e1))
print(e1.__class__)
print(e1.__dir__)
#print(e1.__mro__)

#print(type(e1))

e1.turnupper()
e1.show()