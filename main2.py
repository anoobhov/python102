# This code helps us to deceide whether we should go out or not

# print("Please enter today's whether conditions: ")
# weather_condition = input()
# """
# If its rainy day or stormy i will not go out
# if cloudy give me a warning message
# if sunny tell him to carry umbrella
# else i will
# """
# if weather_condition == "rainy" or weather_condition == "stormy":
#     print("Please don't go out today")
# elif weather_condition == "cloudy":
#     print("It may rain today")
# elif weather_condition == "sunny":
#     print("Carry umbrella")
# else:
#     print("Go out")

"""
grade card generator
>90 grade s
>80 and<=90 grade a

<40 grade f
"""

print("Enter your marks")
marks = int(input())
if marks > 90:
    print("Grade is S.")
elif marks > 80:
    print("Grade is A")
elif marks > 70:
    print("Grade is B.")
else:
    print("Grade is F.")
