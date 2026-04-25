def hello():
    print("Hello world")
hello()

##-----funtion with parameter
def summation(a,b):
    result= a+b
    return result
total = summation(51, 89)
print(total)

#------funtion with default parameter

def summation(a=0, b=0):
    result= a+b
    return result
total=summation(10,20)
print(total)

def user_info(fname='Md', lname='Azim'):
    print(f"First Name:{fname}, Last Name: {lname}")
user_info(lname="Korim", fname="Md")
user_info()