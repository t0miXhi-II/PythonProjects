import os
import csv

name = input("Enter your name: ")
team = input("Enter team name: ")


with open("phonebook2.csv", "a") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow([name, team])