# Polymorphism
# Overriding

class bird(object):
    def __init__(self):
        pass
    def fly(self):
        print("some birds can fly")

class sparrow(bird):
    def __init__(self):
        pass
    def fly(self):      #fly is accessable to sparrow but here we are overriding
        print("sparrow can fly")

class ostrich(bird):
    def __init__(self):
        pass
    def fly(self):
        print("Ostrich can't fly")

class pigeon(bird):
    def __init__(self):
        pass

sparrow = sparrow()
ostrich=ostrich()
pigeon=pigeon()

sparrow.fly()
ostrich.fly()
pigeon.fly()
