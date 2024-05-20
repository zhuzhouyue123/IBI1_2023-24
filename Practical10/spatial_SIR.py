#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   spatial_SIR.py
@Time    :   2024/05/18 03:33:54
@Author  :   Zhu Zhouyue 
@Version :   1.0
@Contact :   zhouyue.23@intl.zju.edu.cn
@Desc    :   None
'''

# here put the import lib
import numpy as np
import matplotlib.pyplot as plt

# init
N = 100  # size
beta = 0.3  
gamma = 0.05 
num_time_steps = 100

# init population
population = np.zeros((N, N))

# randomly choose a infected person
initial_infected = np.random.choice(range(100),2)
population[initial_infected[0],initial_infected[1]] = 1

# stimulation
for t in range(num_time_steps):
    # get the position of the infected
    infected_rows, infected_cols = np.where(population == 1)
    for row, col in zip(infected_rows, infected_cols):
        # neighbors
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if i == 0 and j == 0:
                    continue
                new_row, new_col = row + i, col + j
                if 0 <= new_row < N and 0 <= new_col < N:
                    if population[new_row, new_col] == 0:
                        population[new_row, new_col] = np.random.choice([0,1],1,p=[1-beta,beta])[0]
    # recoveries
    recovered_rows, recovered_cols = np.where(population == 1)
    for row, col in zip(recovered_rows, recovered_cols):
        population[row, col] = np.random.choice([1,2],1,p=[1-gamma,gamma])[0]

# draw the figure
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.show()