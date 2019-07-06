import numpy as np
from matplotlib import pyplot as plt
from quickMafs import quickMafs

def main():

    np.set_printoptions(precision = 3, suppress = True) #3 sigfigs, no sci notation
    a = np.linspace(1,20,12) #create some sample data
    a = a.reshape(6,2) #1D -> 2D
    var_data = quickMafs(a) #construct object

    print(a + '\n') #view the sample data

    print(var_data.mean()) #view the sample data attributes
    print(var_data.median())
    print(var_data.mode())
    print(var_data.st_dev())

    var_data.linePlot() #create a line plot
    var_data.scatterPlot() #scatter plot
    var_data.barChart() #bar chart

main()