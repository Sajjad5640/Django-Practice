list2 = [-1,2,3,-4,5,6,7,-8,9,-10]
positive = []
negative = []
for n in list2:
    if n>0:
        positive.append(n)
    else:
        negative.append(n)
print(positive)
print(negative)