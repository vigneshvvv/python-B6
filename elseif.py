a = int(input("Enter a number A: "))
b= int(input("Enter a Number B: "))
operation = int(input("Enter a operation to perform 1. Add 2. Sub 3.multiplication 4.Division"))

if(operation == 1):
    print(a+b)
elif (operation == 2):
    print(a-b)
elif(operation == 3):
    print(a*b)
elif (operation == 4):
    print(a/b)
else:
    print("Invalid Operation")