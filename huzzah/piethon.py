
import csv
from team import Team

def read_csv():
    with open('PWHL_goals_2023.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
                Team(lines[0])
                print(lines[0])
            

def main():
     read_csv()
     print("hello")

main()