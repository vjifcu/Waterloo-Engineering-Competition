import loaddata, forecast, outputresults
import os

this_dir = os.path.dirname(os.path.realpath(__file__))

def main():
    #First we load the raw csv data
    try:
        data_dir = this_dir + "/sourcedata/"
        raw_data = loaddata.loadRawIntoDict(data_dir)
    except KeyError as e:
        print(str(e))
        print("Could not load data\n")
        exit()
    
    print(raw_data['1998']['69']['130']['Ambient Air Temperature'])
    
    #We now perform analysis on the data set
    forecast.analyzeRaw(raw_data)

    #Finally we output results for the selected day/month
    outputresults.outputDay()

if __name__ == '__main__':
    main()