import pandas as pd
import numpy as np

# data = np.genfromtxt('/Users/apple/desktop/py4e/ImportData1/titanic_sub.csv', delimiter = ',', names=True,dtype=None)
# print(data)
# print(np.shape(data))
# print(data['Fare'])
# print(data['Survived'])

#recfromcsv is similar to genfromtxt but the arg dtupe=True is default
d = np.recfromcsv('/Users/apple/desktop/py4e/ImportData1/titanic_sub.csv', delimiter=',', names=True)
