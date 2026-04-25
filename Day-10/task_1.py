fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
freq = {}

for fruit in fruits:
    if fruit in freq:
        freq[fruit]+=1
    else:
        freq[fruit] = 1
print(freq)