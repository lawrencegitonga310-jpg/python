# A cictionary is a data type that stores data in terms of key - value pair.
# it is introduced by the use of curly braces{}
# The values stored inside a dictionary can be of any data type.
# To access the values in a dictionary we use the keys.


phonebook= {
    "Lawrence" : "2549898898990",
    "Martine" : "254756894567",
    "Liam"   :  "254890789099"
}
# Showing the entire diictionary
print(phonebook)
print(type(phonebook))

# printing lawrence number
print(phonebook["Lawrence"])

# .......................................................................

player = {
    "name": "Messi",
    "age" :  40 ,
    "team": ["PSG","Barcelona", "Argentina"],
    "more" :{
        "children":3,
        "residence":"US",
        "phone" :(3546463656,45456443,434454343)
    }
}
# print barcelona
print(player["team"][1])

# print messi second number
print("Messi second number is :",player["more"]["phone"][1])
