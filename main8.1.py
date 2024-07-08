#Codes without the use of inheritance


# class car:
#     def __init__(self):
#         self.fuel_capacity=0
#         self.number_of_tyre=0
#         self.color="blue"
#         self.music_system= True
#
#     def refuel(self):
#         pass
#     def accelerate(self):
#         pass
#     def rear_door_open(self):
#         pass
#
# class bike:
#     def __init__(self):
#         self.fuel_capacity=0
#         self.number_of_tyre=0
#         self.color="red"
#         self.helmet_color="red"
#     def refuel(self):
#         pass
#     def accelerate(self):
#         pass
#     def do_wheelie(self):
#         pass



#using inheritance

class vehicle(object): #--->vehicle class is called the base class

#(like us can also write like) class vehicle: (this would also exucute the same way)
    self.fuel_capacity = 0
    self.number_of_tyre = 0
    self.color = "blue"

    def refuel(self):
        print("refuel")
    def accelerate(self):
        pass
class car(vehicle):
    def __init__(self):
        self.music_system= True
        vehicle.__init__(self)

    def rear_door_open(self):
        pass
    def travel_long_distance(self,refuel):
        super(car,self).refuel()

class bike(vehicle):
    def __init__(self):
        self.helmet_color="red"
        vehicle.__init__(self)
    def do_wheelie(self):
        pass