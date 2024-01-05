def sq(n):
    i = 1
    while i<= n:
        yield i*i
        i += 1
temp = sq(10)
print(temp.__next__())
print(temp.__next__())
print(temp.__next__())
print(temp.__next__())
print(temp.__next__())
print(temp.__next__())
