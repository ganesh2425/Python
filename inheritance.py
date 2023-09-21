'''
sinle inheritance
multilevel inheritance
multiple inheritance
hierachical inheritance 
'''

# single inheritance
class parent():
    def output(self):
        print("i am the parent")
class child(parent):
    def outputc(self):
        print("i am the child")

c=child()
c.outputc() #child method
c.output() #parent method

#multilevel inheritance
class grandFather():
    def output(self):
        print("i am grandfather")
class parent(grandFather):
    def outputp(self):
        print("i am parent")
class child(parent):
    def outputc(self):
        print("i am child")
c= child()
c.output()
c.outputp()
c.outputc()

# multiple inheritance
class father():
    def output(self):
        print("Iam father")
class mother():
    def outputm(self):
        print("Iam mother")
class child(father,mother):
    def outputc(self):
        print("Iam child!")
d =child()
d.output()
d.outputm()
d.outputc()

# hierachical inheritance
class father():
    def output(self):
        print("I father")
class child1(father):
    def outputm(self):
        print("I child1")
class child2(father):
    def outputc(self):
        print("I child2")
d =child1()
d2 = child2()
d.output()
d.outputm()
d2.outputc()
d2.output()