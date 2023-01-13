import csv

with open("students.csv", "r") as file:
    for line in file:
        age = int(line[2])
        if age < 30:
            print(f"{row[0]} {row[1]}: {row[2]}")