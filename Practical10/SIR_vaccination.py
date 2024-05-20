#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   SIR_vaccination.py
@Time    :   2024/05/10 02:41:49
@Author  :   Zhu Zhouyue 
@Version :   1.0
@Contact :   zhouyue.23@intl.zju.edu.cn
@Desc    :   None
'''

# here put the import lib
import numpy as np
import matplotlib.pyplot as plt

# variables
def SIR(rate):
    N = 10000
    S = int(9999*(1-rate))
    I = 1
    beta = 0.3
    gamma = 0.05
    I_array = []
    for t in range(1000): # time loop
        # randomly pick people to become infected
        contact_rate = beta * I / N
        if contact_rate > 1:
            print(N,S,I)
            print(contact_rate)
        infections = np.random.choice([1,0], S, p=[contact_rate, 1-contact_rate])
        new_I = infections.sum()
        # randomly pick people to be recoveries
        recoveries = np.random.choice([1,0], I, p=[gamma, 1-gamma])
        new_R = recoveries.sum()
        S -= new_I
        I = I + new_I - new_R
        # record the changes
        I_array.append(I)
    return I_array

vaccinate_rate_list = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

# draw
plt.figure(figsize=(6,4), dpi=150)
for rate in vaccinate_rate_list:
    plt.plot(SIR(rate), label=f"{rate*100}%")
plt.xlabel("time")
plt.ylabel("number of people")
plt.legend()
plt.title("SIR model with different vaccination rates")
# plt.show()
plt.savefig("./SIR_model_vaccination.png")