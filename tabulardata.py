#! /usr/bin/env python3

import pandas as pd
import sys
import matplotlib.pyplot as plt
import scipy
from scipy import stats

def data_regression_plot(data, *argv):
    data = pd.read_csv("iris.csv")
    print("iris.csv")
    plot_data(data, *argv)
    regression_plots(data, *argv)


def mat_plot(data, *argv):
#Credit: Jamie Oaks
    dataframe = pd.read_csv("iris.csv")
    plt.scatter(dataframe.petal_length_cm, dataframe.sepal_length_cm)
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.savefig("petal_v_sepal_length.png")


__name__=='__main__'
