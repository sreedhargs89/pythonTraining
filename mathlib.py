def add(a,b):
	print (a+b)
	print("Book keeper=",__name__)

def minus(a,b):
	print (a-b)

def mult(a,b):
	print (a*b)

def quot(a,b):
	print (a/b)

def wrapper(fnptr, *args, **kwargs):
	print ("hello world")
	fnptr(*args,*kwargs)
	print ("bye world")


'''

1. __pycache_file will be created when we load the module
2. Any python program we run its namespace/bookkeeper name is always "__main__"
1.e
		__name__ == "__main__"

Method1:
import mathlib
Bookkeeper holds - All data, variables and metadata

add
minus
mult
quot


'''
