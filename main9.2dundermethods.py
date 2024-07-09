class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def __add__(self, other):
        return self.marks+other.marks   #equivalent to anubhav.add(anurag)

    def __truediv__(self, other):
        return self.marks/other.marks

    def __str__(self):
        # return "Name is "+ self.name+" marks is "+ str(self.marks)
        # return "Name is {name} and marks is {marks}".format(name=self.name,marks=self.marks)
        return f"Name is {self.name} and marks is {self.marks}"

    #

anubhav=student("Anubhav",100)
anurag=student("Anurag",87)

print(anurag+anubhav)
print(anubhav/anurag)

print(anurag)   #now let's give objects display name