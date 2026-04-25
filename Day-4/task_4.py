
operator = input().strip()
a = int(input())
b = int(input())

if operator == '+':
    print(a + b)
elif operator == '-':
    print(a - b)
elif operator == '*':
    print(a * b)
elif operator == '/':
    if b == 0:
        print("Error")
    else:
        print(a / b)  