# python list
# is a list of collection of items that are ordered in acertain way 
# A list is introduced by the use of the square brackets[]
# the items of a list are stored inside of indexes.note:in programming we start counting from index zero (0),bmw, benze, hiance
# a list is mutable i.e the content of a listcan be changed

cars=["BMW","Benz","Hiance","Prado","probox","Mclarel","Range"]

print(cars)
print(type(cars))

# Accessing items of a list
print(cars[2])
print("the car on index four is:",cars[4])

# list slicing: this is creating a list from a given bigger list
print(cars[4:])

# printing from zero index three
print(cars[:4]) 

# printing from hiance to probox
print(cars[2:5])

# list- mutability
# we use the function append to add an item at the end of of a list
cars.append("Mercedes")
print(cars)

cars.append("subaru")
print(cars)

# #we use the pop function to remove an item at the end of the list
cars.pop()
print(cars)

#we can use an index to add items to a list
cars[5] ="pajero"
print(cars)

# we can use sort function to sort out items in alphabetical order
cars.sort()
print(cars)

del cars[4]
print(cars)

cars.pop(4)
print(cars)

cars.remove("BMW")
print(cars)