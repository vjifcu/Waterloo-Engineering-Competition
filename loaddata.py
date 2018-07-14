import csv
import os


def loadRawIntoDict(data_dir):
    raw_dict = {}
    field_list = {'Net Radiometer': 5, 'Ambient Air Temperature': 9}

    for csv_file in os.listdir(data_dir):
        with open(data_dir + csv_file) as file_handle:
            reader = csv.reader(file_handle)
            raw_list = list(reader)
        
        for row in raw_list:
            #First add year to dictionary if not present
            if not row[1] in raw_dict:
                raw_dict[row[1]] = {}
            #Next add month
            if not row[2] in raw_dict[row[1]]:
                raw_dict[row[1]][row[2]] = {}
            #Next add day
            if not row[3] in raw_dict[row[1]][row[2]]:
                raw_dict[row[1]][row[2]][row[3]] = {}
            for field in field_list.keys():
                raw_dict[row[1]][row[2]][row[3]][field] = row[field_list[field]]

    return raw_dict
    #Dictionary format: year = {month = {day = {time = {data}}}} 

