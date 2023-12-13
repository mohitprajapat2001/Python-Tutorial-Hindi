#To Create Dynamic Array Takes Value User, Searching in Array
from array import *

vals = array("i", [])

nums = int(input("Enter The Size of Array : "))

for i in range(nums):
    temp = int(input("Enter the Value of Array :"))
    vals.append(temp)

print(vals)

# Searching of a Value in Array

tst = int(input("Enter the Value For Search"))
k = 0
for i in vals:
    if i == tst:
        print(f"{tst} is Found")
        print(f"{tst} Index = {k}")
        break
    k += 1
else:
    print("Not Found")

print(vals.index(tst))
