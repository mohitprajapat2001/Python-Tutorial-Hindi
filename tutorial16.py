#Global vs Locaal Variable
a = 10
def scope():
    # global a
    a = 9
    print("Inside Function",a, id(a))
    x = globals()['a']
    print("Globlas",x,id(x))
    x = 5
    print(x)
scope()
print("Outside Function",a, id(a))
