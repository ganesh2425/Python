c = ()
print(type(c))

a = (2,4,66,7,7,56,5,89,"amazon")
print(a[-1])
print(a[0:4:2])


b = (3,55,7,98,172,76,43)
print(min(b))
print(max(b))
print(sum(b))
print(len(b))

# concat
t1 = (2,3,4)
t2 = (5,6,7)
print(t1+t2)

#repeat
s1 = (2,4,6,3,9,8)
print(s1*4)

#iteration
for i in s1:
    print(i)

# membership
a1 = (3,4,5,6,7,9)
print(3 in a1)
print(11 not in a1)

b2 = (2,3,4)
b3 = (2,3,4)
b4 = (5,6,7)
print(b2 is b3)
print(b3 is not b4)