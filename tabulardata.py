#! /usr/bin/env python3

import pandas as pd
import sys
import matplotlib.pyplot as plt
import scipy
from scipy import stats

def data_regression_plot(data, *argv):
    data_plot(data, *argv)
    regression_plot(data, *argv)


def data_plot(data, *argv):
    dataframe=pd.read_csv(data)
#Credit: Jamie Oaks, joaks1/python-tabular-data
    for arg in argv:
        plt.scatter(dataframe.petal_length_cm, dataframe.sepal_length_cm)
        plt.xlabel("Petal length (cm)")
        plt.ylabel("Sepal length (cm)")
        plt.savefig("petal_v_sepal_length.png")
        plt.clf()

def regression_plot(data, *argv):
#Credit: Jamie Oaks, joaks1/python-tabular-data
    dataframe = pd.read_csv(data)
    for arg in argv:
        x = dataframe.petal_length_cm
        y = dataframe.sepal_length_cm
        regression = stats.linregress(x, y)
        slope = regression.slope
        intercept = regression.intercept
        plt.scatter(x, y, label = 'Data')
        plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
        plt.xlabel("Petal length (cm)")
        plt.ylabel("Sepal length (cm)")
        plt.legend()
        plt.savefig("petal_v_sepal_length_regress.png")

__name__=='__main__'
