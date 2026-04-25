status = input("Pass or Fail (p/f): ")

if status == "p":
    print("Pass")
    mark = int(input("Enter a number : "))

    if mark>80:
        print("A+")
    elif mark>70:
        print("A")
    elif mark>60:
        print("B")
    else:
        print("Fail")
else:
    print("Tmi Fail")

