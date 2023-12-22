class A:
    def feature1(self):
        print("I am Feature 1")
    def feature2(self):
        print("I am Feature 2")

class B:
    def feature3(self):
        print("I am Feature 3")
    def feature4(self):
        print("i am Feature 4")

class C(A,B):
    def feature5(self):
        print("I am in Feature 5")

a1 = A()
a1.feature1()
# a1.feature1()
# a1.feature2()
b1 = B()
b1.feature3()
c1 = C()

c1.feature2()
