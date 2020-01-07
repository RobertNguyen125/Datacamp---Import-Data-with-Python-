#numpy can be used to load data as array (numerical data)
# http://yann.lecun.com/exdb/mnist/ minst dataset

import numpy as np
import matplotlib.pyplot as plt
filename = 'mnist_kaggle_some_rows.csv'
digits = np.loadtxt('/Users/apple/desktop/py4e/ImportData1/mnist_kaggle_some_rows.csv', delimiter =',')
# print(digits)

im =digits[21,1:]
im_sq = np.reshape(im, (28,28))
# print(im_sq)
# print(im)

# plt.imshow(im_sq, cmap='Reds',interpolation='nearest')
# plt.show()


#2: customising numpy ImportData1
data = np.loadtxt('/Users/apple/desktop/py4e/ImportData1/seaslug.txt', delimiter='\t',dtype=str)
# print(data)
# print(data[0])

#import data as floats and skip the first row
data = np.loadtxt('/Users/apple/desktop/py4e/ImportData1/seaslug.txt', delimiter = '\t', dtype='float',skiprows=1)
print(data[9])
plt.scatter(data[:,0], data[:,1])
plt.xlabel('time(min.)')
plt.ylabel('percentage of larvae')
plt.show()
