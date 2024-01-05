class Students:
    school = "Mohit Coding School"
    #Instance Method
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    #Class Method
    @classmethod
    def getschoolname(cls):
        print(cls.school)

    #Static Method
    @staticmethod
    def info():
        print("This is Static Methods")

s1 = Students(10,20,30)
s2 = Students(15,30,45)


print(s1.avg())
Students.getschoolname()
Students.info()
s1.info()
