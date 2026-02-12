# Test 1
# By use of a function that accepts parameters, calculate the simple interest given principal as 45000, rate is 7% and the time taken is 8 years. (si = p*r*t/100)
# Use the same function inside of a loop to calculate two other simple interests. Note use your own principal, rate and time.

#def simpleinterest():
    # num1 = int(input("Enter the principle :"))
    # num2 = int(input("Enter the rate :"))
    # num3 = int(input("Enter the time :"))
    # simpleinterest = num1 *num3*(num2/100)
    # print("The answer is:",simpleinterest)

# simpleinterest()

print("=====================")
def multiply(principle,rate,time):
    product=principle*time*rate/100
    print("the product is:",product)

multiply(4500,7,8)

