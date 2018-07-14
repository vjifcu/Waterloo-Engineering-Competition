import numpy as np

def outputDay():
    maxTemp = [30, 35, 32, 34]
    minTemp = [15, 12, 8, 10]
    np.savetxt('outputData.csv', (maxTemp, minTemp), fmt='%.1d', delimiter=',')