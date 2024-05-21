#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   SIR.py
@Time    :   2024/05/12 00:54:45
@Author  :   Zhu Zhouyue 
@Version :   1.0
@Contact :   zhouyue.23@intl.zju.edu.cn
@Desc    :   None
'''

# here put the import lib
import numpy as np
import matplotlib.pyplot as plt

# variables
S = 9999
I = 1
R = 0
beta = 0.3
gamma = 0.05
N = 10000

# init arrays to record changes
S_array = []
I_array = []
R_array = []

for t in range(1000): # time loop
    # randomly pick people to become infected
    contact_rate = beta * I / N
    infections = np.random.choice([1,0], S, p=[contact_rate, 1- contact_rate])
    new_I = infections.sum()
    # randomly pick people to be recoveries
    recoveries = np.random.choice([1,0], I, p=[gamma, 1-gamma])
    new_R = recoveries.sum()
    
    S -= new_I
    I = I + new_I - new_R
    R += new_R

    # record the changes
    S_array.append(S)
    I_array.append(I)
    R_array.append(R)

# draw the figure
plt.figure(figsize=(6,4), dpi=150)
plt.plot(S_array, label="susceptible")
plt.plot(I_array, label="infected")
plt.plot(R_array, label="recovered")
plt.xlabel("time")
plt.ylabel("number of people")
plt.legend()
plt.title("SIR model")
plt.savefig("./SIR_model.png")