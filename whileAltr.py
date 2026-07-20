user = "Vignesh"
passwordN = "Vignesh"
attempts = 1
isLogin = False

while(attempts < 4):
    userName = input("Enter your userName: ")
    password = input("Enter your password: ")

    if userName == user and passwordN == password:
        print("login successful")
        isLogin = True
        break
    else:
        print(f"Either userName or password incorrect. attempts remaining: {3-attempts}")
        attempts += 1

if isLogin == False:
    print("Maximum attempts Reached. Try after sometime")