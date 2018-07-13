import csv
import os


def loadRawIntoDict(data_dir):
    raw_dict = {}

    for csv_file in os.listdir(data_dir):
        with open(data_dir + csv_file) as file_handle:
            reader = csv.reader(file_handle)
            raw_list = list(reader)
        
        for row in raw_list:
            print(row[1])
            if not row[1] in raw_dict:
                raw_dict[row[1]] = {}


    #Dictionary format: year = {month = {day = {time = {data}}}} 

