'''

lists
'''

v = []
print(type(v))

x = [2,5,7,55,88,24,"kiran"]
print(x)
print(x[4])
print(x[-1])
print(x[0:4:2])

'''

append
extend
count
pop
insert
remove
index
'''

x = [2,4,7,55,88,24,"kiran"]
x.append("pyhton")
print(x)
x.extend([4,67,4,6,445,78,0])
print(x)
print(x.count(4))
x.remove(55)
print(x)
x.pop(4)
print(x)


z = [3,6,66,989,24,654,98]
print(z.index(989))

for i in [3,6,66,989,24,654,98]:
    print(i)

z.insert(0,"xyz")
print(z)