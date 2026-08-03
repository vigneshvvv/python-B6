import csv

with open("studentDetails.csv", "a", newline="") as file:
    writer = csv.writer(file)
    
    writer.writerow([106, "John", "ECE"])