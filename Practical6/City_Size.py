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

# here put the import lib
import matplotlib.pyplot as plt

# cities = {"Country": {"City": Population}}
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

uk_population = list(cities["UK"].values())
cn_population = list(cities["China"].values())
uk_population.sort()
cn_population.sort()
print(uk_population)
print(cn_population)

fig, (uk_axs, cn_axs) = plt.subplots(2, sharey=True, figsize=(6,8))

fig.suptitle("City Size")

uk_bar = uk_axs.bar(cities["UK"].keys(), cities["UK"].values())
uk_axs.set_ylabel("Population (millions)")
uk_axs.bar_label(uk_bar)

cn_bar = cn_axs.bar(cities["China"].keys(), cities["China"].values())
cn_axs.set_ylabel("Population (millions)")
cn_axs.bar_label(cn_bar)

plt.show()
plt.clf()
