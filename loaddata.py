import csv
import os


def loadRawIntoDict(data_dir, field_list):
    raw_dict = {}
    year_col = None
    day_col = None
    time_col = None

    for csv_file in os.listdir(data_dir):
        with open(data_dir + csv_file) as file_handle:
            reader = csv.reader(file_handle)
            raw_list = list(reader)
        
        firstRow = 1
        for row in raw_list:
            if firstRow:
                firstRow = 0
                for val in row:
                    if val == 'Year':
                        year_col = firstRow
                    elif val == 'Julian Day':
                        day_col = firstRow
                    elif val == 'Time':
                        time_col = firstRow
                    elif val == 'Ambient Air Temperature':
                        field_list['Ambient Air Temperature'] = firstRow
                    elif val == 'Precipitation (Tipping Bucket)':
                        field_list['Precipitation (Tipping Bucket)'] = firstRow
                    firstRow = firstRow + 1
                firstRow = 0
            else:
                #First add year to dictionary if not present
                if not row[year_col] in raw_dict:
                    raw_dict[row[year_col]] = {}
                #Next add month
                if not row[day_col] in raw_dict[row[year_col]]:
                    raw_dict[row[year_col]][row[day_col]] = {}
                #Next add day
                if not row[time_col] in raw_dict[row[year_col]][row[day_col]]:
                    raw_dict[row[year_col]][row[day_col]][row[time_col]] = {}
                for field in field_list.keys():
                    raw_dict[row[year_col]][row[day_col]][row[time_col]][field] = row[field_list[field]]
    return raw_dict
    #Dictionary format: year = {month = {day = {time = {data}}}}

