# Printing the string and numbers use of sep and end
print("hello world")
print("Hello world", "I am anubhav", sep=".")

print(21)
print(10, end=" ")
print(20, 30, 40, sep=",")

# The code bellow add two numbers
t = 'a'
x = 10  # python is weakly typed language so it doesn't need to specify type of variable
y: int = 20  # but we can explicitly define variable(if we want (not necessary))
print("The sum of the numbers is:", x+y)

""" Multi line 
    comments """
multi_line_string = """
Hello world
this is a multi line string
"""
print(multi_line_string)

# taking input from the user
print("Hello now we will do a demo of a calculator")
print("Enter first number", end=" ")
first_number = int(input())  # the console would take input as a string but we converted to integer

print("Enter second number", end=" ")
second_number = int(input())
print("The sum of the numbers is: ", first_number+second_number)

# let see the changing the type and viewing the type of any variable
a = "1024"
b = int(a)
print(type(b))
c = 'a'
n = chr(ord(c) + 10)
print(n)


# now se the ascii values
s = "A"
print(ord(s))

# type casting
q = 23
w = 34
print("The sum of q and w", q + w)
print("The typecasting of q and w", str(q)+str(w))
