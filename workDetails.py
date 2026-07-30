class Address:
    def __init__(self, state, city):
        self.state = state
        self.city = city
    
class Employee:
    def __init__(self, name, age, salary, state, city):
        self.name = name
        self.age = age
        self.salary = salary
        self.address = Address(state, city)

employees = [
    Employee("John", 25, 30000, "TN", "Chennai"),
    Employee("Bob", 30, 50000, "TN", "Madurai"),
    Employee("Alice", 35, 60000,"TN", "Trichy"),
    Employee("David", 28, 45000,"TN", "Chennai")
]

result = list()
for employee in employees:
    if employee.age > 30:
        result.append(employee)
        print(employee.__dict__)


resultN = list(filter(lambda e: e.age>30, employees))
print(resultN[0].name)

resultF = [e for e in employees if e.age > 30]
print(resultF[0].name)

resultName = [e.name for e in employees if e.age<30]
print(resultName)

sorted_list = sorted(employees, key=lambda e: e.salary, reverse=True)
print(sorted_list[0].name)
print(sorted_list[1].name)


highest = max(employees, key=lambda e: e.salary)
print(highest.__dict__)

minimum = min(employees, key=lambda e: e.salary)
print(minimum.__dict__)

isPresent = any(e.salary>70000 for e in employees)
print(isPresent)

isAvailable = all(e.salary > 50000 for e in employees)
print(isAvailable)

fFirst = next(e for e in employees if e.age > 25)
print(fFirst.__dict__)

noOfEmp = len([e for e in employees if e.age > 25])
print(noOfEmp)

totalSalary = sum(e.salary for e in employees)
print(totalSalary)

empInCh = list(filter(lambda emp: emp.address.city == "Chennai", employees))
print(empInCh[0].__dict__)
