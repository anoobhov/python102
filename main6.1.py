# file = open("sample.txt","r")
# content = file.read()
# # print(line)
#
# # converting into arrays of lines
# lines=content.split("\n")
# print(lines)
#
# for line in lines:
#     print(line)
#
# file.close()


# file = open("sample.txt","w")
# file.writelines(["Hello\n","I am writing in the opened file"])
# file.close()

# file = open ("sample.txt", "a")
# file.write("\nThis is some new lines i am adding to the sample.txt file\n")
# file.write("Now as the file is in append mode hope it doesn't erase the previous ones")

#file reading and appending at the same time

# file2 = open("sample.txt","a")
#
# file2.write("\n\n\nCan I do editing and reading files in one go??")
# file1 = open("sample.txt","r")
# print(file1.read())
#
# file2.close()
# file1.close()

import json
# with open("config.json","r") as f:
#     configuration =json.load(f)
#     print(configuration["environment"])
#     print(configuration["database_port"])

with open("json_dump.json","w") as f:
    d = {
        "port" : 3006,
        "image_location": "httds...",
        "student_records": [
            "Soham",
            "XYZ"
        ]
    }