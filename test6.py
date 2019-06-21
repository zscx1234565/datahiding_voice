import pynamical
import random
from pynamical import simulate, bifurcation_plot, save_fig
import pandas as pd, numpy as np, IPython.display as display, matplotlib.pyplot as plt, matplotlib.cm as cm

num=30
ini_value = random.uniform(0, 1)
rate = random.uniform(3.6, 4)
pops = np.zeros((num))
pops[0]=ini_value
for i in range(0,num-1):
    pops[i+1] =pynamical.pynamical.logistic_map(pops[i], rate)
print(pops)

key_seq=[int((a*10000)%9) for a in pops]

print(key_seq)