nums = [1,2,2,3,3,3]

freq = {}

for n in nums:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1

print(freq)
