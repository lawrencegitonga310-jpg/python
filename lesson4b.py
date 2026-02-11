# Loops- sometimes we may need to do a piece of work repeatedly and in such case we may use loop.
# Loop is a control structure that allows us to execute a block of code repeatedly until a certain codition is meet.
# There are two types of loops The for loop and The while loop.

# Below is the syntax of a far loop in python:
"""
for variable in range(n):
    # block of code to be executed 
"""



for greeting in range (5):
    print("hello peter",greeting)


print("=========================")

for number in range(10, 20):
    print(number)

print("=========================")
# find the even number in the range of 50 to 71
for number in range(50, 71, 2):
    print(number)

print("=========================")
# create a python program that prints odd numbers from 100 to 150
for number in range(101, 150, 2):
    print(number)

print("=========================")
# create a python program that prints the multiples of three from 201 to 150
for number in range(201, 150, -3):
    print(number)
    
print("=========================")
# create a python program that prints the leap year in between 2000 and 2024
for number in range(2000, 2024, 4):
    print(number)
