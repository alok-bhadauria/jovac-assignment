import csv
data = [
    ["Name", "Math", "Science", "English"],
    ["Alok", 85, 90, 95],
    ["Aditya", 90, 85, 75],
    ["Saransh", 85, 85, 85]
]
file = open("students.csv", "w")
cursor = csv.writer(file)

for row in data:
    cursor.writerow(row)
file.close()
print("Data written to 'students.csv'\n")

file = open("students.csv", "r")
reader = csv.reader(file)
print("Reading from 'students.csv':")
for row in reader:
    print(row)
file.close()
