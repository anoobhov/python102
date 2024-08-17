"""
suppose we got a code for where it's likely to get an error.
we beforehand manage that case and avoid the stoppage of the entire code because of that single line
"""
# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print(e.__str__())

# def error_throw_odd(number):
#     if number%2:
#         raise AttributeError("Nummber is odd")
#
#     return
# try:
#     error_throw_odd(5)
# except AttributeError as e:
#     print(e.__str__())


import logging
logger=logging.getLogger("Error logger")
class error_catching:
    def __init__(self):
        self.arr=[1,2,3,4,5]

    def get_value_for_index(self,index):
        if index<0:
            raise AttributeError("Index is negative")
        if index>len(self.arr):
            raise AttributeError("Index out of bound")
        return self.arr[index]

e=error_catching()

while True:
    print("Enter ur choice")
    print("1.Enter the index")
    print("2.Exit")

    ch=int(input())

    if ch == 2:
        break

    else:
        try:
            index=int(input())
            print(e.get_value_for_index(index))
        except AttributeError as e:
            logger.error(e)