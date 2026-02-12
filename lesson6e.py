
# zero division error

# on the try and except block:you run some codes /statement and if it is successful the block will executed other the exept block will be executed when there is an anticipated error

try:
     number = 100
     answer = number /0
     print("The answer is :",answer)
except Exception as e:
     print("There is an error:",e)



