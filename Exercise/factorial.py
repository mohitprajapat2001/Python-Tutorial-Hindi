#Faactoial of a Number
num = int(input("Enter Your Number"))

def fact(x):
    f = 1
    for i in range(1, x+1):
        f = i*f
    print(f"Factorial of {x}",f)

fact(num)
