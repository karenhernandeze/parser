# Function used to import the transition table from csv. The return format is a list. 
import csv

def transitions_table():
    # open file where the transitions table is as a csv file
    with open('table/transitions_table.csv', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        lst = list(reader)
        # print(lst)
        return lst
    
transitions_table()