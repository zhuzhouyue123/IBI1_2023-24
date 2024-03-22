#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   City_Size.py
@Time    :   2024/03/19 16:22:40
@Author  :   Zhu Zhouyue 
@Version :   1.0
@Contact :   zhouyue.23@intl.zju.edu.cn
@Desc    :   None
'''

# This program will print out the population lists of two countries and generate two bar_figure in one big figure

# here put the import lib
import matplotlib.pyplot as plt

# cities = {"Country": {"City": Population}}   Data Structure
cities = {  # Create a multi-dimensional dictionary to store the population info
    "UK": {
        "Edinburgh": 0.56,
        "Glasgow": 0.62,
        "Stirling": 0.04,
        "London": 9.7    
    },
    "China":{
        "Haining": 0.58,
        "Hangzhou": 8.4,
        "Shanghai": 29.9,
        "Beijing": 22.2
    }
}

# This part will selected the population values and store it in two lists.
uk_population = list(cities["UK"].values())
cn_population = list(cities["China"].values())
# Sort the values
uk_population.sort()
cn_population.sort()
# Print it out in the terminal
print(uk_population)
print(cn_population)

# Use plt.subplots() to generate figure object and subplots objects.
fig, (uk_axs, cn_axs) = plt.subplots(2, sharey=True, figsize=(6,8))

# Set the figure title
fig.suptitle("City Size")

# configure the uk_population's sub-figure
uk_bar = uk_axs.bar(cities["UK"].keys(), cities["UK"].values())
uk_axs.set_ylabel("Population (millions)")
uk_axs.bar_label(uk_bar)

# configure the cn_population's sub-figure
cn_bar = cn_axs.bar(cities["China"].keys(), cities["China"].values())
cn_axs.set_ylabel("Population (millions)")
cn_axs.bar_label(cn_bar)

# show the img
plt.show()
plt.clf()
