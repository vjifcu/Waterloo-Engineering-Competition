import loaddata, forecast, outputresults


def main():
    #First we load the raw csv data
    try:
        raw_data = loaddata.getDict()
    except LOADERROR:
        print("Could not load data\n")
        exit
    
    #We now perform analysis on the data set
    forecast.analyzeRaw()

    #Finally we output results for the selected day/month
    outputresults.outputDay()