class A:
    def __init__(self):
        print("I am in Class A")

# class B(A):
class B:
    def __init__(self):
        # super().__init__()
        print("I am in Class B")
    def featureb(self):
        print("I am Feature B")

class C(B,A):
    pass

# a1 = A()
# b1 = B()
c1 = C()
