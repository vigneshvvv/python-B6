user = "Vignesh"
passwordN = "Vignesh"
attempts = 1

while attempts > 0:
    if attempts == 4:
        print("Maximum attempts reached. pls try again after sometime")
        break

    userName = input("Enter your userName: ")
    password = input("Enter your password: ")

    if(userName == user and passwordN == password):
        print("Login successful")
        break
    else:
        print(f"Either userName or password incorrect. Attempts remaining: {3-attempts}")
        attempts += 1

