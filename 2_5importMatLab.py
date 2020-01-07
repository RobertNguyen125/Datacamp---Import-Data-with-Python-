import scipy.io
import numpy as np
import matplotlib.pyplot as plt

mat = scipy.io.loadmat('/Users/apple/desktop/py4e/importData1/albeck_gene_expression.mat')
print(type(mat))

for k,v in mat.items():
    print(k,v)
