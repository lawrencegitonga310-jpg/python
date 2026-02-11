# a for loop can also be used to iterate through a list, tuple,string or even a dictionary

name = "lawrence"

for letter in name:
    if letter =="n":
     print("the letter is n")
else:
    print(letter)

    # below is a list of counties
    counties = ["Nairobi","Mombasa","Kisumu","Eldoret","Kajiado","machakos","Meru"]

    print(counties)

    for county in counties:
       print(county)

print("================================")
 
if "Meru" in counties:
   print("Found the county")
else:
   print("not found")
   
   
print("================================")
for county in counties:
   if "Meru" in counties:
      print("The county is part of the list")
      break
   else:
      print("The county is not part of the list")

# the loop can also be used in iterate through a dictionary


player = {
   "name": "Mbappe",
   "age" : 25,
   "team": ["PSSG","Monaco","France"],
   "nationality": "french"
}

for key in player:
   print(key)

print("================================")
for value in player:
   print(player[value])

print("================================")
# loop the teams the player has played for
for team in player["team"]:
   print(team)