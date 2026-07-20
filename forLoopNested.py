userName = ["Vignesh", "Sathish", "Venkat", "Deva"]
password = ["Vignesh@212", "Sathish@545", "V@1112", "DevaNathan"]

userIn= input("Enter your userName: ")
passWord = input("Enter your password: ")

status = False

for user in userName:
    for p in password: 
        if(user == userIn and p == passWord):
            status = True
    

if(status):
    print("Data Available")
else:
    print("Data Not Avaiable")
       
        