import numpy as np
import matplotlib.pyplot as pit
import pandas as pd

datasheet = pd.read_csv("Data.csv")
print(datasheet[0:6][3:][:-1])
print()
x = datasheet.iloc[:,:].values
a = datasheet.iloc[:,:-1]
print(x)
print(a)