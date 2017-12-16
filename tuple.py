tab = [1,2,3,4,5][::2]

print(tab)

li = [1,2,3,4,5]

print(li)
li[1] = 12

print(li)



a= ('a', 'b', 'c')

print(a)

s = 'asdasd'

print(s)

s = set(s)

print(s)


a=[x for x in range(1000) if x%10==0]

print(a)

def g():
    for i in range(1000):
        yield i


a = g()

print(a.next())

print(a.next())

print(a.next())


a = [1,2,3,4,5]

import copy

b = copy.copy(a)

print(a,b)

a[3] = 221

print(a,b)

i = range(1,11)

for i in i:
    print(i)
else:
    print('koniec')


for x in range(11,18):
    print('lec dalej')
    continue


print 12

x = {'A':1, 'B':2}

for i in x.keys():
    print x[i]
