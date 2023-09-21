'''
block of code
'''

def func(): # function definition
    print("Hello Bangalore!!") # function body

func() # function call


# def fun(x,y,z):
#     print("Python world!",x,y,z)
# fun(2,3,4)

def fun(*x):
    print("Python world!",x)
fun(2,3,4)

def fun(**x):
    print("Python world!",x)
fun(x=4,y=7)

#nested function
def outer():
    print("outer function")
    def inner():
        print("inner function")
    inner()
outer()

def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)