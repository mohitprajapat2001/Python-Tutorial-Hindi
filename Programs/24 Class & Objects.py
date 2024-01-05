class Car:
    #Attributes
    brand = "XYZ"
    Model = "XYZ"
    Engine = 350
    #Methods
    def info(self):
        print(self.Model, self.brand, self.Engine)


c1 = Car()
c2 = Car()

print(c1)
# print(c2)

# print(c1.brand, c1.Model, c1.Engine)
c1.brand = "Hyundai"
c1.Model = "Sentro"
c1.Engine = 600
# print(c1.brand, c1.Model, c1.Engine)

# print(c2.brand, c2.Model, c2.Engine)
c2.brand = "Tata"
c2.Model = "Harrier"
c2.Engine = 900
# print(c2.brand, c2.Model, c2.Engine)

print(c1.info())
print(c2.info())

