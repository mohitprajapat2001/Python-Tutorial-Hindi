#DeepCopy Interview Point of View Important
import copy
from copy import deepcopy



# a = 10
# b = a
# print("a ",a, id(a))
# b = 8
# print("b ",b, id(b))

lst1 = [1,2,3,4]
lst2 = copy.deepcopy(lst1)
print(id(lst1))
print(id(lst2))
print(lst1)
print(lst2)

lst2[1] = 5
print("lst2",lst2)

lst2[3] = 5
print("lst2",lst2)

print("lst1",lst1)
