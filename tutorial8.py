#Patterns
# print("* * * *")
# print("* * * *")
# print("* * * *")
# print("* * * *")
test1 = int(input("Enter Number of Rows and Colums"))
for i in range(test1):
    for j in range(test1):
        print("*",end=" ")
    print()

#Pattern 2
for i in range(8):
    for j in range(i+1):
        print("*",end=" ")
    print()

#Pattern 2 but in Reverse

for i in range(4):
    for j in range(4-i):
        print("*",end=" ")
    print()
