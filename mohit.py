class Hello:
    def __init__(self,a , b, c):
        self.a = a #public
        self._b = b #Protected
        self.__c = c #Private

    #Getter Method
    def getvalues(self):
        print(self.a, self._b, self.__c)

    #Setter Method
    def setvalues(self, value):
        self.__c = value


a1 = Hello(2,4,6)

# a1.__c = 8
a1.setvalues(10)
a1.getvalues()
