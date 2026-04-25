# #----Arbitary argument

# def student_name(*names):
#     print(len(names))
#     print(type(names))
# student_name("rohim", "Korim", "Jodu","modu")

def mr_cars(**cars):
    print(cars['model'])
car_info={
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
}
mr_cars(** car_info)