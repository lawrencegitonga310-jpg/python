# Qn 1: Function Without Parameters 
# Create a function that: 
# • Takes no parameters 
# • Uses arithmetic operators to calculate the area of a rectangle 
# • Prints the result 
def area():
    length = 10
    width = 6
    area = length * width
    print("The area of the rectangle is:",area)

area()
print("====================================")
# Qn 2: Function With Parameters 
# Create a function that: 
# • Accepts two numbers as parameters 
# • Returns their sum, difference, product, and division 
def arithmetic_operation(num1, num2):
    sum= num1+num2
    difference=num1-num2
    product= num1*num2
    division=num1/num2
    return sum, difference, product, division

result=arithmetic_operation(16,5)
print("the sum is:",result(0))
print("the difference is:",result(1))
print("the product is:",result(2))
print("the division is:",result(3))

print("====================================")
# Qn 3: Control Statement (if...elif...else) 
# Write a function that: 
# • Accepts a number (use input function) 
# • Checks whether the number is: 
# • Positive 
# • Negative 
# • Zero 
def check_number():
  num=int(input("Enter a number:"))
  if num>0:
     print("The number is positive")
  elif num<0:
     print("The number is negative")
  else:
     print("The number is neutral")

check_number() 

print("====================================")
# Qn 4: Loop with Arithmetic 
# Write a function that: 
# • Accepts a number n 
# • Uses a for loop 
# • Calculates the sum of numbers from 1 to n 
def sum_of_number(n):
   sum=0
   for i in range(1, n+1):
      sum+=1
      print("The sum of number from 1 to",n,"is:",sum)
      n=int(input("Enter a number:"))

      sum_of_number(n)

print("====================================")
# Qn 5: While Loop 
# Write a function that: 
# • Accepts a number (Use input() function) 
# • Uses a while loop 
# • Calculates the square of numbers from 1 up to that number 



