'''
wrapping of variables methods in a single unit is called Encapsulation
public
private __
protected _
'''

class demo():
    __a=2 #private
    _b=4   #protected
    print(__a)
    print(_b)

# class demo2():
#     def __init__(self,x,y):
#         self.__x=x #private
#         self._y=y #protected
# class demo3(demo2):
#     def output(self):
#         print(self._y)
# d=demo3(3,4)
# d.output()

def add(a,b):
    print(a+b)
add(2,5)
add('a','b')
add([56,98],[5,8])
add((6,9),(3,8))
        