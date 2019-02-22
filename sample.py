import mathlib
import vendors.intel
import vendors.sony
import vendors.subvendors.nokia

## For package cases we can import modules directly
from vendors import *

with this you can call
intel.intelm()
sony.sonym()
subvendors.nokia.nokiam()




print(dir(mathlib))
print(mathlib.add(1,4))
print("Current or local bookkeeper name: "+__name__)

vendors.intel.intelm();
