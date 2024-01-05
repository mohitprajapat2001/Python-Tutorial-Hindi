# a = 2
# # b = 5
# b = "Mohit"
#
# try:
#     print(a+b)
# except Exception as e:
#     print("Cant Add string with Number", f"{e}")
#
# print("Bye")


a = 6
# b = "mohit"
b = 8
def div(a,b):
    try:
        print("In Try Block")
        print(a/b)
        return "No Error"
    except Exception as e:
            print("In Exception Block")
            print("Error", f"{e}")
            return "Error"
    finally:
        print("Done")


x = div(a,b)
print(x)
# except ZeroDivisionError:
#     print("Cant Divide by Zero")
# except TypeError:
#     print("Enter Numbers")






