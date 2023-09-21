# s = {2,3,5,55,5}
# print(type(s))


s = {2,44,5,2,456,56,77,32,77,90,0,1}
'''
add
update
pop
remove
'''
print(s)
#add
s.add(364)
print(s)

#update
s.update({67,87,4,20})
print(s)

#pop
s.pop()

#remove
s.remove(456)
print(s)

'''
union
intersection
difference
issubset
issuperset
'''

# union
set1 ={1,2,3}
set2 ={4,5,6}
print(set1.union(set2))

#intersection
p1 ={2,3,4,5}
p2 ={4,6,7,8}
print(p1.intersection(p2))

#difference
s1 ={1,2,3,4}
s2 ={4,5,6,7}
print(s1.difference(s2))
print(s2.difference(s1))



for i in {1,2,3,4,5}:
    print(i)