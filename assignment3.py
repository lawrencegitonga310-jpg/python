# Below is a  statement based on what a student will have gotten
Grossincome = float(input("Enter the Gross income: "))
# print("The entered marks is",marks)
if Grossincome>0 and Grossincome <=5.999:
    print("Contribution is: 150.00")

elif Grossincome >=6000 and Grossincome <=7.999:
    print("Contribution is: 300.00") 

elif Grossincome>=8000 and Grossincome <=11999:
    print("Contribution is: 400.00")   

elif Grossincome >=12000 and Grossincome <=14999:
    print("Contribution is: 500.00") 

elif Grossincome >=15000 and Grossincome <=19999:
    print("Contribution is 600.00")

elif Grossincome >=20000 and Grossincome <=24999:
    print("Contribution is: 750.00") 

elif Grossincome >=25000 and Grossincome <=29999:
    print("Contribution is: 850.00")
elif Grossincome >=30000 and Grossincome <=49999:
    print("Contribution is: 1000.00") 

elif Grossincome >=50000 and Grossincome <=99999:
    print("Contribution is: 1500.00")  
else:
    print("Contribution is :2000.00") 
