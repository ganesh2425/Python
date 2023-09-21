'''
open

read/write

close

'''
#read
s=open('demo.txt', mode='r')
print(s.read())
s.close()

#write
x=open('demo.txt', mode='a')
x.write("bye bye write!")
x.close()

#read/write r+
x=open('demo.txt', mode='r+')
print(x.read())
x.write("r+ mode turn on")
x.close()

#write/read w+
x=open('demo.txt', mode='w+')
x.write("w+ mode!")
print(x.read())
x.close()