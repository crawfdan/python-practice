import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

class quickMafs:

    def __init__(self, data): #initialize object, pass in 2D array
        self.data = data

    def mean(self): #return the mean of all data in array
        return np.mean(self.data)

    def median(self): #return the median of all data in array
        return np.median(self.data)

    def st_dev(self): #return the standard deviation of all data in array
        return np.std(self.data)

    def mode(self): #return the mode of all data in array
        return stats.mode(self.data, axis=None)
    
    def linePlot(self): #simple line plot
        plt.plot(self.data[:,0], self.data[:,1]) #use first value as x and second value as y in each nested list
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Line Plot")
        plt.show()

    def scatterPlot(self): #scatter plot of data with black dots
        plt.plot(self.data[:,0], self.data[:,1], "ko") 
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Scatter Plot")
        plt.show()

    def barChart(self): #bar chart that takes two sets of data for x and y
        plt.bar(self.data[:,0], self.data[:,1])
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Bar Chart")
        plt.show()


