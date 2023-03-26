#! /usr/bin/env python3

import sys
import re
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

#Okay, I was too big for my britches. I think I got most of the variable calls right in the last one but it just wouldnt work
#So we're hard-coding

dataframe = pd.read_csv("iris.csv")

#First species: Setosa
setosa = dataframe[dataframe.species == "Iris_setosa"]
setosa_x = setosa.petal_length_cm
setosa_y = setosa.petal_length_cm
plt.scatter(setosa_x, setosa_y, label = 'Data')
set_reg = stats.linregress(setosa_x, setosa_y)
plt.plot(setosa_x, set_reg.slope * setosa_x + set_reg.intercept, color = "purple", label = "Fitted Line")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.savefig("setosa_petal_v_sepal_length_regress.png")

#Second species: Versicolor
versicolor = dataframe[dataframe.species == "Iris_versicolor"]
versicolor_x = versicolor.petal_length_cm
versicolor_y = versicolor.petal_length_cm
plt.scatter(versicolor_x, versicolor_y, label = 'Data')
set_reg = stats.linregress(versicolor_x, versicolor_y)
plt.plot(versicolor_x, set_reg.slope * versicolor_x + set_reg.intercept, color = "purple", label = "Fitted Line")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.savefig("versicolor_petal_v_sepal_length_regress.png")

#Third species: Virginica
virginica = dataframe[dataframe.species == "Iris_virginica"]
virginica_x = virginica.petal_length_cm
virginica_y = virginica.petal_length_cm
plt.scatter(virginica_x, virginica_y, label = 'Data')
set_reg = stats.linregress(virginica_x, virginica_y)
plt.plot(virginica_x, set_reg.slope * virginica_x + set_reg.intercept, color = "purple", label = "Fitted Line")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.savefig("virginica_petal_v_sepal_length_regress.png")
