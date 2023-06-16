# Function used to import the transition table from csv. The return format is a list. 
import csv

def parsing_table():
    # open file where the transitions table is as a csv file
    with open('table/parsing_table.csv', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        lst = list(reader)
        # print(lst)
        return lst
    
parsing_table()