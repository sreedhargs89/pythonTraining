##this is the example
##program of the python tutorial

"""
########## BEST Practices for the beginners  ################

1. Never save ur program in the installation directory, it treat your program as libraries
This leads to slower module search
2. Never use the inbuilt funtion names as user defined variables. sum/max/min/list/tupple/Set
3. Always variable name is lower case
4. Never mangle with inbuilt variables
5. YOur extentension is .py
6. On Unix/Linux/Mac - Sha-bang is compulsary(#!)
"""


import os #load the library
import sys

print ("My PID - ", os.getpid())
print ("My File Name - ", sys.argv[0])

num = input ("Enter a number : ")
ans = int(num) * int (num)
print ("Ans = ", ans)



##int-class:-
##==========

"""
num = 10     -- decimal
num - 0b10   -- binary
num = 0o10   -- Octal
num = 0xFFFF -- hexa


print(bin(num))
print(hex(num))
print(oct(num))


num = "20"
num = int(num)

num = "11111" # binary string
num= int(num, base=2)

## Getting first unit from the integer
num=12345
num[0] -- not possible
print(str(num)[0])  -- convert to string and get it 

"""


b=2.5
h=3.6

a = 1/2 * b * h;

print (a)










