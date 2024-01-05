#Map

l = [1,3,8,9,4,6,2]
# newl = []
# for i in l:
#     newl.append(i*i)
# print(newl)

# def double(x):
#     return x*x

# newl = list(map(double, l))
newl = list(map(lambda x: x*x, l))
print(newl)

#Filter

newnewl = list(filter(lambda x : x%2==0, newl))

print(newnewl)


#Reduce
from functools import reduce

mysum = reduce(lambda x,y : x+y, newnewl)
print(mysum)
