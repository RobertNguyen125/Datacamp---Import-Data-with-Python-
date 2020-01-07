import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = '/Users/apple/desktop/py4e/ImportData1/titanic_sub.csv'
df = pd.read_csv(file)
#print(df.head())

file = '/Users/apple/desktop/py4e/ImportData1/mnist_kaggle_some_rows.csv'
data = pd.read_csv(file, nrows=5,header=None)
#print(data.head())
data_array=np.array(data)
#print(type(data_array))

file = '/Users/apple/desktop/py4e/ImportData1/titanic_corrupt.txt'
d = pd.read_csv(file, sep ='\t', comment='#', na_values='Nothing')
print(d.head())

# plot Age variable histogram
pd.DataFrame.hist(d[['Age']])
plt.xlabel('Age(year)')
plt.ylabel('count')
plt.show()

#the histogram shows that the majoriy of the passenger is in 20-40 years old range
