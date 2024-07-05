# records=[("Soham",100),("Anubhav",23),("Aurag",123)]
# queries=["Soham","Anubhav","Aurag"]
# for query in queries:
#     for record in records:
#         if record[0] == query:
#             print(record[1])


#dictornaries
records = {
    "Soham": 100,
    "Anubhav":123,
    "Kunal": 23,
}
queries=["Soham", "Anubhav", "Kunal"]
for query in queries:
    print(records[query])

records.pop("Anubhav")

# iteration in records
for key in records.keys():
    print(key)
    print(records[key])

# Aother way to declare a record
r=dict()

# Keys storing arrays

temp ={
    "anubhav": [23,45],
    "aryan": [32],
    "sammer":[34,221,1223,224]
}

#keys as pairs(u can't have list as they are unhashables)
d = {
    (10,29): "aNUBHAV RAJ",
    (33,11): "Aerospace"
}

print(d[(10,29)])

