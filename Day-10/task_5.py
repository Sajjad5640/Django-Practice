name = input("Enter name Sazzad or Azim:")
Phonebook = {"Sazzad": "017xx", "Azim": "018xx"}
# for a,b in Phonebook.items():
#     if a == "Sazzad":
#         print(b)
#     else:
#          print(b)
def search_number(name,**Phonebook):
    if name in Phonebook:
        print(Phonebook[name])
    else:
         print(Phonebook[name])
search_number(name,**Phonebook)



