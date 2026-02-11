# Python functions
# they are blocks of code/statement that performs a given task/action.They can be reused through out the program to perform different tasks.
# Functions are defined using the def keyword (define)
# We have two main types of functions.
# 1.  In-built functions -> They come preinstalled with the interpreter i.e print(), pop(), range(), append() etc...
# 2. User defined functions => They are created by a programmer to solve a given task.
# To define a function you need to give it a name followed by parenthesis.
# For the functions, it is usually indented and to invoke a function we use the function name.


def greetings():
    print("Hello, how are you?")
# if i indent there will be no output
# below we call the function by use of its name
greetings()

print("================================")
# Additional function 
def addition():
    num1 =40
    num2 =50
    sum = num1 + num2
    print("The sum of the number is:",sum)

addition()

print("================================")
# below is division function 
def divide():
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    quotient = num1 / num2
    print("The answer is:",quotient)
    print("-----")


for function in range(3):
    divide()

