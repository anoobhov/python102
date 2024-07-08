class A(object):
    def work(self):
        print("Work in A")

class  B(A):
    def work(self):
        print("Work in B")

class C(A):
    def work(self):
        print("Work in C")
    pass

class D(B, C):  #here b is given more priority than C as it's the way its written in D(B,C)
    pass        #like that's the precedent order even though both B & C are on same level


d=D()
d.work()