import pandas as pd
from sas7bdat import SAS7BDAT
import matplotlib.pyplot as plt

with SAS7BDAT('/Users/apple/desktop/py4e/importData1/sales.sas7bdat') as file:
    df_sas=file.to_data_frame()

print(df_sas.head())

pda.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()
