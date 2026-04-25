nums= [1, 2, 2, 3, 1, 4]
# list = set(nums)
# print(list)
un_num = []
for n in nums:
    if n not in un_num:
        un_num.append(n)
print(un_num)
