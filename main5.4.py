# #strings
# string="Anubhav Raj"
# print(string[0])
#
# string_seperate=string.split(" ")
# print(string_seperate)
# first_name,last_name=string.split(" ")
# print(first_name)
#
# # method 1
# inp=input()
# seperated_integers= inp.split(" ")
# print(seperated_integers)
# for i in range(len(seperated_integers)):
#     seperated_integers[i]=int(seperated_integers[i])
# print(seperated_integers)
#
# #method 2
# arr=list(map(int,input().split()))
# print(arr)

"""
u are given a date in form of 7/7/2024
return it in 07-07-2024
"""
def prettify_date(date_string):
    date_string=date_string.split("/")
    for i in range(len(date_string)):
        date_string[i]=date_string[i].zfill(2)
    return date_string[0]+"-"+date_string[1]+"-"+date_string[2]

print(prettify_date("7/7/2024"))
