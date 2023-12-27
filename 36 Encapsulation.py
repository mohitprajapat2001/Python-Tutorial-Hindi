class Car:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color

    def getcolor(self):
        return self.__color
    def setcolor(self, value):
        self.__color = value

    def getspeed(self):
        return self.__speed
    def setspeed(self, value):
        self.__speed = value

ford = Car(200, "red")
bmw = Car(400, "black")
# ford.speed = 300
# print(ford.color, ford.speed)
# print(bmw.color, bmw.speed)
# ford.__color = "Pink"
ford.setcolor("Yellow")
print(ford.getcolor(), ford.getspeed())
print(bmw.getcolor(), bmw.getspeed())
