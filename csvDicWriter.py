import csv

new_student = {
    "id": 107,
    "name": "Bob",
    "Department": "CSE"
}

with open("studentDetailsN.csv", "a", newline="") as file:
    fields = ["id", "name", "Department"]
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerow(new_student)