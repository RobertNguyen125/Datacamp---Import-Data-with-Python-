import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_stata('/Users/apple/desktop/py4e/importData1/disarea.dta.txt')
print(df.head())

pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extend of disease')
plt.ylabel('Number of countries')
plt.show()
