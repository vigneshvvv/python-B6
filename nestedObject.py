class Coordinates:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng


class Address:
    def __init__(self, state, city, lat, lng):
        self.state = state
        self.city = city
        self.coordinates = Coordinates(lat, lng)

class EmployeeDetails:
    def __init__(self, emp_id, emp_name, department, state ,city, lat, lng):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.department = department
        self.address = Address(state, city, lat, lng)

emp = EmployeeDetails(1, "vignesh", "DEV", "TN", "Chennai", -77.16213, -77.16213)
print(emp.address.state)
print(emp.address.coordinates.lat)
print(emp.address)