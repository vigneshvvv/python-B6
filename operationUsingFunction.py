users = [{
    "userName": "Vignesh",
    "password": "Vignesh@123",
},
{
    "userName": "Sathish",
    "password": "Sathish@123"
},
{
    "userName": "Deva",
    "password": "Devanathan@121"
}]

def login():
    attempts = 1
    while(attempts > 0):
        if(attempts == 4):
            print("Number of attempts exceeded. pls try again after sometime")
            break

        userN = input("Enter your userName: ")
        passwordN = input("Enter your password: ")
        loggedIn = False

        for user in users:
            if user["userName"] == userN and user["password"] == passwordN:
                loggedIn = True
                break
        if loggedIn:
            print(f"login successful. Welcome back {userN}")
            break
        else:
            print("Either userName or password is incorrect. pls try again")
            attempts += 1

def registration():
    firstName = input("Enter your firstName")
    lastName = input("Enter your lastName")
    userNameN = input("Enter a userName")
    ispresent = False

    for user in users:
        if user["userName"] == userNameN:
            print("userName already exist. redirecting to login")
            ispresent = True
            login()
            break
    if ispresent:
        return
    else:
        passwordN = input("Enter your password: ")
        reEnter = input("Re-Enter your password: ")
        if passwordN == reEnter:
            users.append({
                "userName":  userNameN,
                "password": passwordN
                })
        else:
            print("Re-entered password doesn't match")

        
operation = input("Enter operation you want to perform 1.login 2.registration ")
if operation == "1":
    login()
elif operation == "2":
    registration()
else:
    print("Invalid operation. please choose right one")