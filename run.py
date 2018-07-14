import loaddata, forecast, guiIO

import os

this_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = this_dir + "/sourcedata/"
field_list = {'Net Radiometer': 5, 'Ambient Air Temperature': 9}
raw_data = None


def main():
    print('Shutting down...')



#This method is run each time the user clicks the run button
def predict(year, day):
    #First we load the raw csv data
    try:
        raw_data = loaddata.loadRawIntoDict(data_dir, field_list)
    except FileNotFoundError as e:
        print(str(e))
        print("Could not load data\n")
        exit()
    
    #Get input fields
    input_selections = {'year': year, 'day': day}
    
    #We now perform analysis on the data set
    min_temp, max_temp = forecast.analyzeRaw(raw_data, input_selections)

    #Finally we output results for the selected day/month
    guiIO.outputResult("Historical daily low: " + str(min_temp) + "\nHistorical daily high: " + str(max_temp))


if __name__ == '__main__':
    main()