class A(object):
    def __init__(self):
        self.name="Class A"
        self.id=20

class B(A):
    def __init__(self):
        A.__init__(self)    #calling the base constructor
        self.name="Class B"
        self.id=30

class C(A):
    def __init__(self):
        self.name="Class C"
        self.id=10
        A.__init__(self)
        """ 
        basically what happed here is that 
        self.name="Class C"
        self.id=10
        (constructor A is called)
        then
         self.name="Class A"
        self.id=10
        """


b=B()
c=C()

print(b.name,b.id)
print(c.name,c.id)      #why did C printed A attributes instead of it's own
