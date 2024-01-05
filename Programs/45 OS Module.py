import os
# print(os)
# cwd = os.getcwd()
# print(cwd)

# os.chdir("D:/")
# print(os.getcwd())

# print(os.listdir("D:/"))

# path = os.path.join(cwd, "Temp")
# os.mkdir(path)

# os.chdir("D:/Python Tutorial/Temp")
# print(os.getcwd())

# open("New.txt", "w")

# os.rename("New.txt", "My.txt")

# print(os.path.getsize("My.txt"))


os.chdir("D:/Python Tutorial")
print(os.getcwd())

path = os.path.join(os.getcwd(), "Temp")
os.rmdir(path)
