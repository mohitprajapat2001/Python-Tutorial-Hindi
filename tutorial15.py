#Types of Argument

# *args
# def add(*b):
    # print(a)
    # print(type(b))
    # print(b)
    # c = 0
    # for i in b:
    #     c += i
    # print(c)

# add(5,7,8,9,11,14)

# def person(name, age=18):
#     print(name)
#     print(age)
#
# person("Mohit", 24)

# **kwargs
def user(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)

user("mohit",age=25,city="Jaipur",tel=88888)
