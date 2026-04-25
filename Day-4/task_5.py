
registration = input().strip().lower()  
attendance = int(input())

if registration == "no":
    print("Not Allowed (Not Registered)")
elif registration == "yes" and attendance >= 75:
    print("Allowed")
else:
    print("Not Allowed (Low Attendance)")