import numpy as np
import h5py
import matplotlib.pyplot as plt

data = h5py.File('/Users/apple/desktop/py4e/importData1/LIGO_data.hdf5','r')
print(type(data))

for key in data.keys():
    print(key)

group=data['strain']
for key in group.keys():
    print(key)

#set variable equal to time series data: strain
strain =data['strain']['Strain'].value
#set number of time points to sample: num_samples
num_samples = 10000
#set time vector
time = np.arange(0,1,1/num_samples)

plt.plot(time, strain[:num_samples])
plt.xlabel('GPS TIME(s)')
plt.ylabel('strain')
plt.show()
