#! /usr/bin/env python3

import pandas as pd
import sys
import matplotlib.pyplot as plt
import scipy
from scipy import stats

def data_regression_plot(data, *argv):
    plot_data(data, *argv)
    regression_plots(data, *argv)


__name__=='__main__'
