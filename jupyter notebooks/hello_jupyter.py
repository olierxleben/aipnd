#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 100, 100)
plt.plot(x, np.cos(x))
plt.show() 

plt.plot(x, np.sin(x))
plt.show()