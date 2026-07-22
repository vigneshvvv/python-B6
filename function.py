def sampleAddition():
    print("function working")


def loginCheck(username, password):
    if username == "Sathish" and password == "Sathish":
        print(f"Hi Welcome {username}")

def multiple(a, b):
    c = a*b
    return c


sampleAddition()
loginCheck("Sathish", "Sathish")
result = multiple(10,20)

if (result %2 == 0):
    print("Even number")
else:
    print("odd number")