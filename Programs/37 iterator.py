# lst = [5, 6, 8, 7, 9, 4]
# print(lst)
# for items in lst:
#     print(items)
#
# temp1 = iter(lst)
# temp2 = lst.__iter__()
# print(temp1)
# print(temp2)

# print(next(temp1))
# print(next(temp1))
# print(next(temp1))
# print(next(temp1))
# print(next(temp1))
# print(next(temp1))
# print(next(temp1))

#Custom Iterator
class CounterTen:
    def __init__(self, limit):
        self.num = 1
        self.limit = limit
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= self.limit:
            temp = self.num
            self.num += 1
            return temp
        else:
            raise StopIteration

a1 = CounterTen(250)
# print(next(a1))
# print(next(a1))
# print(next(a1))
# print(next(a1))
# print(next(a1))
for i in a1:
    print(i)






















