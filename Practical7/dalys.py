#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   public_health.py
@Time    :   2024/03/29 09:41:38
@Author  :   Zhu Zhouyue 
@Version :   1.0
@Contact :   zhouyue.23@intl.zju.edu.cn
@Desc    :   None
'''

# here put the import lib
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dalys_raw = pd.read_csv("./dalys-rate-from-all-causes.csv")

# 1-100, every 10 rows
print(dalys_raw.iloc[0:101:10,3])

# DALYs of Afghanistan
dalys_afghanistan = dalys_raw.loc[dalys_raw["Entity"] == "Afghanistan", "DALYs"]
print(dalys_afghanistan)

# DALYs of China
dalys_china = dalys_raw.loc[dalys_raw["Entity"] == "China", ["Entity","Year","DALYs"]]
print(dalys_china)
# Calculate the mean value
china_mean_dalys = dalys_china["DALYs"].mean()
print(f"The mean DALYs of China is {china_mean_dalys}")
# DALYs in China in 2019 is less than the mean

# Draw the plot
plt.plot(dalys_china.Year, dalys_china.DALYs)
plt.title("DALYs of China")
plt.show()

# Additional Question
dalys_uk = dalys_raw.loc[dalys_raw["Entity"] == "United Kingdom", ["Entity","Year","DALYs"]]
print(dalys_uk)

# Draw the plot
plt.plot(dalys_uk.Year, dalys_uk.DALYs)
plt.title("DALYs of UK")
plt.show()