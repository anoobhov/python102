# class dog:
#
#     def set_name(self,name):
#         self.name = name
#     def bark(self):
#         print(self.name," is barking")
#     def run(self):
#         print(self.name," is running")
#
# tommy = dog()
#
# tommy.set_name("tommy")
# tommy.run()
# tommy.bark()


# class dog:
#
# # constructor in ppython
#     def __init__(self):
#         print("Calling the constructor")
#         self.name =""
#     def set_name(self,name):
#         self.name= name
#     def run(self):
#         print(name,"is running")
#
# tommy = dog()

# class dog:
#
#     def __init__(self,name,breed,age):      #parameterized constructor
#         print("Calling the constructor")
#         self.name=name
#         self.breed= breed
#         self.age=age
#     def run(self):
#         print(self.name,"is running")
#     def get_details(self):
#         print("---------Generating the details------------")
#         print("Name: ",self.name)
#         print("Breed: ",self.breed)
#         print("age: ",self.age)
#
# tommy= dog("TOMMY","human",45)
# tommy.get_details()



# class dog:
#
#     def __init__(self,name):      #parameterized constructor
#         print("Calling the constructor for ",name)
#         self.name=name
#
#     def __del__(self):
#         print("Calling the deconstrutor for ",self.name)
#
#
# tommy= dog("TOMMY")
# if True:
#     print("Inside the if statement")      #if u declare a variable inside a block if, for
                                     #it would still have outside scope as python doesn't have block scope
#     max=dog("Maxx")
# print("Outside the if statement")


class dog:

    def __init__(self,name):      #parameterized constructor
        print("Calling the constructor for ",name)
        self.name=name

    def __del__(self):
        print("Calling the deconstrutor for ",self.name)

def f():
    print("Function started")
    tommy=dog("tommy")      #destructor is called as soon as object goes out of the scope

f()
print("Outside the f function")
