# a = 10
# print(b)

try:
    print('b') #risky code
except:
    print("error")
else:
    print("no error")
finally:
    print("always")


try:
    print('a'+33)
except TypeError:
    print("type error")
except ValueError:
    print("value error")