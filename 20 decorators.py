# def mfx(fx):
#     def ifx(*args, **kwargs):
#         print("Hello I am Starting this Function")
#         fx(*args, **kwargs)
#         print("Thanks for using this function")
#     return ifx
#
# @mfx
# def greet():
#     print("Hello Mohit")
#
# @mfx
# def sum(a,b):
#     print(a+b)
#
# greet()
# sum(5,6)

def smartdiv(fx):
    def ifx(a,b):
        if a<b:
            a,b = b,a
        fx(a,b)
    return ifx
@smartdiv
def div(a,b):
    print(a/b)

div(3,6)
