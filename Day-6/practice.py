my_dict = {
    "course":"WADP",
    "batch":"1st",
    "fee": 0
}
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
#-----------loop
for data in my_dict.values():
    print(data)
for data in my_dict.items():
    print(data)
for a,b in my_dict.items():
    print(f"key is : {a},value is : {b}")