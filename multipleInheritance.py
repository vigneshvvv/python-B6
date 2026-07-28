class Employee:
    def __init__(self, emp_id, emp_name):
        self.emp_id = emp_id
        self.emp_name = emp_name

class Address:
    def __init__(self, state, city):
        self.state = state
        self.city = city

class Developer(Employee,Address):
    def __init__(self, emp_id, emp_name,state, city, language):
        Employee.__init__(self,emp_id, emp_name)
        Address.__init__(self,state,city)
        self.language = language

dev = Developer(1, "Sathish", "TN", "Chennai", "Java")
print(dev.city)
print(dev.emp_name)


