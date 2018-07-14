import numpy

#Note: We do not account for leap years currently, so some years the days are 1 off, however this is
#       negligible in terms of effect on our data


def analyzeRaw(raw_data, user_request):
    #Wow
    print("Analyzing\n")
    for year in raw_data:
        for day in raw_data[year]:
            day_min, day_max = getMinMax(raw_data[year][day])
            raw_data[year][day]['MinTemp'] = float(day_min)
            raw_data[year][day]['MaxTemp'] = float(day_max)

    #We now retrieve the data for the requested year and day
    #For now average, later, fit value
    to_average = list()
    for year in raw_data:
        to_average.append(raw_data[year][user_request['day']]['MinTemp'])
    average = sum(to_average)/len(to_average)
    print (average)

    to_average = list()
    for year in raw_data:
        to_average.append(raw_data[year][user_request['day']]['MaxTemp'])
    average = sum(to_average)/len(to_average)

    print (average)



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

