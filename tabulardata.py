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

#Credit: Jamie Oaks
for arg in argv:
    dataframe = pd.read_csv("iris.csv")
    plt.scatter(dataframe.petal_length_cm, dataframe.sepal_length_cm)
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.savefig("petal_v_sepal_length.png")
    plt.clf()

def regression_plot(data, *argv):
    dataframe = pd.read_csv(data)
    

__name__=='__main__'
