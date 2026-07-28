class Employee:
    def __init__(self, emp_id, emp_name):
        self.emp_id = emp_id
        self.emp_name = emp_name

class Address(Employee):
    def __init__(self, emp_id, emp_name, state, city):
        super().__init__(emp_id, emp_name)
        self.state = state
        self.city = city

class Manager(Address):
    def __init__(self, emp_id, emp_name, state, city, sizeOfTeam):
        super().__init__(emp_id, emp_name, state, city)
        self.sizeOfTeam = sizeOfTeam


man = Manager(1, "Revanth", "TN", "Chennai", 10)
print(man.state)
print(man.emp_name)