# f = open("data.txt")
# print(f)
# print(f.read(15))
# print(f.readline(10))
# print(f.readline())
# print(f.readline())

# f1 = open("datanew.txt", "w")

# f2 = open("datanew.txt", "a")
#
# f2.write("queen")
#
# file = open("data.txt", "r")
# data = open("datanew.txt", "a")
#
# # print(file.read())
# for i in file:
#     data.write(i)

img = open("myimg.jpg", "rb")
nimg = open("myimg2.jpg", "wb")

for i in img:
    nimg.write(i)

# f1.close()
# f2.close()
# file.close()
# data.close()
img.close()
nimg.close()
print(img.read())





