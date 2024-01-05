#Arrays in Python
from array import *

vals = array("i", [3,4,-2,6,7])

print(vals) #Print Values in Arary
print(type(vals)) #Type Check Array
print(vals[1]) #fetch Index Vales

# For loop to Print Array
for i in vals:
    print(i)

print(vals.buffer_info()) #Returns Addres and Size
print(len(vals)) #Returns Length of Array
print(vals)
vals.reverse()
print(vals)

# While loop to Print Array
i = 0
while i < len(vals):
    print(vals[i])
    i += 1

newarray = array("u", ['a', 'i', 'e', 'o'])
print(newarray)
