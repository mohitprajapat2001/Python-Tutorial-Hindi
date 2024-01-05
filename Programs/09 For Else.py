# # For Else Statement
# lst = [25, 26, 77, 29, 38]
#
# for i in lst:
#     if i%3 == 0:
#         print(i)
#         break
# else:
#     print("not Found")
#
# nlst = [1,2,3,4,5]
# for i in nlst:
#     if i == 3:
#         print("3 is Found !")
#         break
# else:
#     print("0 Is not Found !")
import copy

# Original integers
original_number = 42

# Using id to get the identity of the original integer
original_id = id(original_number)

# Shallow copy using copy.copy()
shallow_copy_number = copy.copy(original_number)

# Deep copy using copy.deepcopy()
deep_copy_number = copy.deepcopy(original_number)

# Modifying the original integer
original_number += 10

# Displaying the results
print("Original Integer:", original_number)
print("Shallow Copy:", shallow_copy_number)
print("Deep Copy:", deep_copy_number)
print()

# Checking the identities
print(f"Original ID: {original_id}")
print(f"Shallow Copy ID: {id(shallow_copy_number)}")
print(f"Deep Copy ID: {id(deep_copy_number)}")
