#Fibonacci Series using Function
num = int(input("Enter the Size of Series: "))
def fib(n):
    lst = [0, 1]
    for i in range(n-2):
        temp = lst[-1] + lst[-2]
        lst.append(temp)
    print(f"Fibanacci Series of {n} Numbers ",lst)
fib(num)
