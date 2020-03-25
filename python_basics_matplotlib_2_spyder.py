# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 19:16:22 2020

@author: silus
"""

import numpy as np
import matplotlib.pyplot as plt

random_array = np.random.randint(0,10, size=(100))
t = np.arange(100)

plt.figure()
plt.plot(t, random_array, label='Noise')
plt.xlabel('Time[s]')
plt.legend()
plt.show()