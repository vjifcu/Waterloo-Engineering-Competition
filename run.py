import loaddata, forecast, outputresults
import os

this_dir = os.path.dirname(os.path.realpath(__file__))


def main():
    data_dir = this_dir + "/sourcedata/"
    field_list = {'Net Radiometer': 5, 'Ambient Air Temperature': 9}

    #First we load the raw csv data
    try:
        raw_data = loaddata.loadRawIntoDict(data_dir, field_list)
    except KeyError as e:
        print(str(e))
        print("Could not load data\n")
        exit()

    #Get input fields
    input_selections = {'year': 1999, 'day': 330}
    
    #We now perform analysis on the data set
    min_temp, max_temp = forecast.analyzeRaw(raw_data, input_selections)

    #Finally we output results for the selected day/month
    outputresults.outputDay()

if __name__ == '__main__':
    main()