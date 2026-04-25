given_data = {
 "Sazzad": 70,
 "Azim": 85,
 "Karim": 60
}
max_val = max(given_data.values())

for a,b in given_data.items():
    if b == max_val:
        print(a)