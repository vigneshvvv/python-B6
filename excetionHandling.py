try:
    lst = [2,1,4,5]
    print(lst[3])
    a = int(input("Enter a age"))
    if a < 18:
        raise ValueError("Age should be greater than 18")
    sample = {
        "Name": "Vignesh",
        "Role": "Dev"
    }
    print(sample["place"])
except IndexError:
    print("Invalid Index")
except ValueError as e:
    print("Enter a valid number")
    print(e)
except KeyError:
    print("Enter a valid key")
except Exception as e:
    print(e)
