# function with parameters
# parameters: they are values that get passed as argument given to a function inside of the parenthesis.


def greeting(name):
    print(f"{name} How are you?Hope everything is fine.")

greeting("Lawrence")
greeting("Jane")
greeting("liam")

print("==============================")
def message(names):
    print(f"Hello {names} .We shall be having a general meeting on data ....please avail yourself.")

message("Lawrence")
message("jane")

print("==============================")
# create function that accepts 
def addition():
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    addition = num1 + num2
    print("The answer is:",addition)

addition()