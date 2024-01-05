class Students:

    def __init__(self, name, rollno, brand, cpu, ram):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop(brand, cpu, ram)

    def show(self):
        print(self.name, self.rollno)
        self.lap.laptopdetails()

    class Laptop:

        def __init__(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram
        def laptopdetails(self):
            print(self.brand, self.cpu, self.ram)


s1 = Students("Mohit", 1, "Hp", "i5", 8)
s2 = Students("Veena", 2, "Lenovo", "i7", 16)
# print(s1.name, s1.rollno)
# s1.show()
# s2.show()

s1.show()
