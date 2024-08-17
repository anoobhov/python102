class student:
    number_of_student=10    #this doesn't change with the objects,it's an class variable
    def __init__(self,name):
        self.name=name      #this would change with every object,it's an instance variable

    def getnameofstudent(self):
        print(self.name)

    @classmethod
    def print_number_of_students(cls):
        print(cls.number_of_student)

    @staticmethod
    def print_helloworld():
        print("Hello world")




AQ=student("AQ")
Er=student("Er")

print(student.print_helloworld())

print(AQ.number_of_student,Er.number_of_student)
print(AQ.name,Er.name)
