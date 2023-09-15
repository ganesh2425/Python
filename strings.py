'''

string is a collection of characters
'''

a = 'pythonlife'
b = "pythonlife"
c = '''pyhtonlife'''

print(type(a),type(b),type(c))

pythonlife = 'please subscribe'
print(pythonlife.upper())

python11 = 'HELLOWORLD!'
print(python11.lower())

python12 = "Hello python"
print(python12.endswith("python"))
print(python12.startswith("H"))

python22 = "python language"
print(python22.replace("language","programming!!"))


python23 = "learning python language"
print(python23.index("python"))
print(python23.find("g"))
print(python23.find("kiran"))


python43 = "hello learning python language"
print(python43.count("l"))
print(python43.removeprefix("hello"))
print(python43.removesuffix("language"))


python55 = "practicing python programming"
print(python55.split())


python65 = "     python language      "
print(python65)
print(len(python65))
v = python65.strip()
print(len(v))
v = python65.lstrip()
print(len(v))
v = python65.rstrip()
print(len(v))