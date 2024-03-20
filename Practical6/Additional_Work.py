#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Additional_Work.py
@Time    :   2024/03/20 13:57:50
@Author  :   Zhu Zhouyue 
@Version :   1.0
@Contact :   zhouyue.23@intl.zju.edu.cn
@Desc    :   None
'''

# here put the import lib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# This is a additional work to generate the box plot of the UK&CN population

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

data = {
    "Countries": ["UK", "UK", "UK", "UK", "CN", "CN", "CN", "CN"],
    "Population": uk_population + cn_population
}
# print(data)

df = pd.DataFrame(data)
# print(df)

sns.boxplot(x="Countries", y="Population", data=df)
plt.show()

