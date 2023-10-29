#Match Statement Feature Python 3.10 <
x = int(input("Enter Your Number : "))

match x:
    case 1:
        print(f"{x} is One")
    case 5:
        print(f"{x} is Five")
    case 7:
        print(f"{x} is Seven")
    case _ if x < 20:
        print(x, "Smaller than 20 Case")
    case _:
        print(x, "Greater than 20 Case")

