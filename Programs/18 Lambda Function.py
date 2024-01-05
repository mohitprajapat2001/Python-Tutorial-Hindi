#Anonymous Functions

# def square(a):
#     return a*a

# f = lambda a : a*a
f = lambda a,b : a+b

a = 5
b = 9
# result = square(a)
# result = f(a)
result = f(a,b)

print(result)
