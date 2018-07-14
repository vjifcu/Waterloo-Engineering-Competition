import numpy as np

#Note: We do not account for leap years currently, so some years the days are 1 off, however this is
#       negligible in terms of effect on our data


#
def analyzeRaw(raw_data, user_request):
    fits = {}
    for year in raw_data:
        for day in raw_data[year]:
            #Get minimum and maximum temperatures
            day_min, day_max = getMinMax(raw_data[year][day])
            raw_data[year][day]['min_temp'] = float(day_min)
            raw_data[year][day]['max_temp'] = float(day_max)
        fits['year'] = {}
        fits['year']['max_temp_fit'] = fitSingleYear(raw_data, year, 'max_temp')
        fits['year']['min_temp_fit'] = fitSingleYear(raw_data, year, 'min_temp')


    #We now retrieve the data for the requested year and day
    #Minimum temperature
    to_average = list()
    for year in raw_data:
        fit_func = fits['year']['min_temp_fit']
        to_average.append(fit_func(user_request['day']))
    average = sum(to_average)/len(to_average)
    avg_min = average

    #Maximum temperature
    to_average = list()
    for year in raw_data:
        fit_func = fits['year']['max_temp_fit']
        to_average.append(fit_func(user_request['day']))
    average = sum(to_average)/len(to_average)
    avg_max = average

    return (avg_min, avg_max)



def getMinMax(day):
    daily_min = None
    daily_max = None
    for time in day:
        #If not yet set add a base value
        if daily_min is None:
            daily_min = day[time]['Ambient Air Temperature']
        if daily_max is None:
            daily_max = day[time]['Ambient Air Temperature']
        #Compare temp to current min/max, set if more extreme
        if float(day[time]['Ambient Air Temperature']) < float(daily_min):
            daily_min = day[time]['Ambient Air Temperature']
        if float(day[time]['Ambient Air Temperature']) > float(daily_max):
            daily_max = day[time]['Ambient Air Temperature']
    return (daily_min, daily_max)


#Takes in raw data for a given field for a given year and generates
#a 5th-order least squares fitted polynomial
def fitSingleYear(raw_data, year, field):
    x = list()
    y = list()

    for day in raw_data[year]:
        x.append(int(day))
        y.append(float(raw_data[year][day][field]))
    coeffs = np.polyfit(x, y, 7)
    return np.poly1d(coeffs)
