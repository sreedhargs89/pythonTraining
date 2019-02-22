import os
import subprocess

res = os.system("ipconfig")

print ("Hello = ",res)

res = subprocess.check_output("dir", shell=True)
print ("Hello = ",res)
