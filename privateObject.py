class UserInfo:
    userId = 0
    __userName = ""
    isAvailable = False
    _lastName = ""

    def __init__(self, userId, isAvailable):
        self.userId = userId
        self.isAvailable = isAvailable

    def getUserName(self):
        return self.__userName

    def setUserName(self, userName):
        self.__userName = userName

user = UserInfo(1, True)
user.__userName = "Vignesh"
user.setUserName("New")

user1 = UserInfo(1, True)
user1.setUserName("New")

print(user.__dict__)
print(user1.__dict__)

