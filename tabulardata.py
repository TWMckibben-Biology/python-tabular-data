#! /usr/bin/env python3

#Load all packages necessary for loading, manipulating, and plotting data
import sys
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy import stats

#Main function for script. Calls lower functions
def data_regression_plot(data, *argv):
    data_plot(data, *argv)
    regression_plot(data, *argv)

#Plots data and exports scatter plot of sepal and petal length
def data_plot(data, *argv):
    dataframe = pd.read_csv('iris.csv')
#Credit: Jamie Oaks, joaks1/python-tabular-data
    for arg in argv:
        splitspecies_df = dataframe[dataframe.species == (arg)]
        plt.scatter(dataframe.petal_length_cm, dataframe.sepal_length_cm)
        plt.xlabel("Petal length (cm)")
        plt.ylabel("Sepal length (cm)")
        plt.savefig("{}petal_v_sepal_length.png".format(arg))
        plt.clf()

#Calculates regression slope and plots it using sepal and petal length
def regression_plot(data, *argv):
#Credit: Jamie Oaks, joaks1/python-tabular-data
    dataframe = pd.read_csv('iris.csv')
    for arg in argv:
        splitspecies_df = dataframe[dataframe.species == (arg)]
        x = splitspecies_df.petal_length_cm
        y = splitspecies_df.sepal_length_cm
        regression = stats.linregress(x, y)
        slope = regression.slope
        intercept = regression.intercept
        plt.scatter(x, y, label = 'Data')
        plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
        plt.xlabel("Petal length (cm)")
        plt.ylabel("Sepal length (cm)")
        plt.legend()
        plt.savefig("{}petal_v_sepal_length_regress.png".format(arg))
        plt.clf()

#Set module
if __name__ == '__main__':
    data_regression_plot(*sys.argv)
