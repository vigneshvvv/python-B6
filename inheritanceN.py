class Employee:
    def __init__(self,emp_id, emp_name):
        self.emp_id= emp_id
        self.emp_name = emp_name

class Developer(Employee):
    def __init__(self, emp_id = 0, emp_name = "",languageKnown = ""):
        super().__init__(emp_id, emp_name)
        self.languageKnown = languageKnown

class Manager(Employee):
    def __init__(self, emp_id, emp_name, sizeOfTeam):
        super().__init__(emp_id, emp_name)
        self.sizeOfTeam = sizeOfTeam


dev = Developer(1, "Vignesh", "Python")
print(dev.emp_id)

man = Manager(2, "Vignesh", 20)
print(man.emp_name)