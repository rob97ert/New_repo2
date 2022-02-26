import numpy as np
import matplotlib.pyplot as plt

for i in range(30):
    print(np.sin(i*np.pi))

aa = np.zeros(30)

for i in range(30):
    aa[i] = i

plt.scatter(aa,aa)