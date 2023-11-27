#Types of Argument

def add(*b):
    # print(a)
    # print(type(b))
    # print(b)
    c = 0
    for i in b:
        c += i
    print(c)

add(5,7,8,9,11,14)

# def person(name, age=18):
#     print(name)
#     print(age)
#
# person("Mohit", 24)
