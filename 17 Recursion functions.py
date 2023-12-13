#Recursion Function in Python
# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())
#
# i = 0
# def bhupendrajogi():
#     global i
#     i += 1
#     print("Naam Bataiye")
#     print("Bhupendra Jogi")
#     print("US Me kaha kaha gaye Hai")
#     print("Bahut Jagah Gya Hu")
#     print(i)
#     bhupendrajogi()
#
# bhupendrajogi()


#Factorials = 5! = 1*2*3*4*5 Recursion Functions

n = 4

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

result = fact(n)
print(result)
