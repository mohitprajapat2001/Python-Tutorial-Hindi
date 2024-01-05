#MEthod Overloading
# class A:
#     def sum(self,a=None, b=None, c=None):
#         if a != None and b != None and c != None:
#             print(a+b+c)
#         elif a != None and b != None:
#             print(a+b)
#         else:
#             print(a)
# a1 = A()
# a1.sum(5, 6, 10)

#Method Overriding
class Student:
    def sum(self, m1, m2):

        print(m1+m2)
class B(Student):
    def sum(self, m1, m2):
        print((m1+m2)/10)

s1 = B()
s1.sum(50,40)










