class Car:
    wheels = 4

    def __init__(self):
        self.Brand = "BMW"
        self.Mileage = 10

print(Car.wheels)
Car.wheels = 5
c1 = Car()
c2 = Car()
print(c1.Brand, c1.Mileage, c1.wheels)
# print(c2.Brand, c2.Mileage)
c1.Brand = "Audi"
print(c1.Brand, c1.Mileage,c1.wheels)
print(c2.Brand, c2.Mileage, c2.wheels)

