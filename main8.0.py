#function overloading by in terms of number of arguements

# def add(x,y,z=0):
#     return x+y+z
#
# print(add(1,2))
# print(add(1,2,3))


#function overloading in terms of no. of usage:
class sparrow:
    def can_fly(self):
        print("Sparrow can fly")

class ostrich:
    def can_fly(self):
        print("Ostrich can't fly")


sparrow=sparrow()
ostrich=ostrich()
for bird in (sparrow,ostrich):
    bird.can_fly()

