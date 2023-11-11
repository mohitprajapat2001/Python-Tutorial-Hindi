#Exercise 1 : Print Number From 1 to 100 using For loop. {b} : And Print Square of that Number
# for i in range(1,101):
#     print(i,end=" Square : ")
#     print(i**2)

#Exercise 2 : Print Sum of Number and Take Input From User using While Loop
# x = int(input("Enter You Range : "))
# sum = 0
# while x > 0:
#     sum = sum + x
#     x = x - 1
# print(sum)

#Exercise 3 : Take Input from User Which is String & Reverse that input using While
test  = input("Enter You Input : ")
x = len(test) - 1
reverse = ""
while x >= 0:
    reverse = reverse + test[x]
    x = x - 1
print(reverse)
