# d ={}
# print(type(d))

d = {1:'abc',34:'ganesh','python':678}
print(d['python'])

'''
get
update
values
keys
items
'''

k = {2:'xyz',56:'hello','age':26}
#get
print(k.get(56))
#keys
print(k.keys())
#values
print(k.values())
#items
print(k.items())
#upate
k.update({568:'ganesh'})
print(k)

for i,j in {1:'abc',34:'ganesh','python':678}.items():
    print(i,j)