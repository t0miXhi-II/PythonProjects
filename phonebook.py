import os
import csv

name = input("Enter your name: ")
#shirt_number = ("Enter shirt number: ")
team = input("Enter team name: ")

with open("phonebook.csv", "a") as file:

    csv_writer = csv.DictWriter(file, fieldnames=["name", "team"])
    csv_writer.writerow({"name": name, "team": team })
