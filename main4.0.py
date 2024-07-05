# Function in python
# Defining a function
def print_message():
    print("Hello in am inside the function")


def add_two_numbers(a, b):
    return a+b


def sub_two_numbers(a, b):
    return a-b


# Calling a function
print_message()
result=add_two_numbers(5,4)
print("sum is ", result)
print("difference is ", sub_two_numbers(7,2))
print("difference is ", sub_two_numbers(b=7,a=2))