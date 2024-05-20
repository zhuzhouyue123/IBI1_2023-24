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

dayls_days = pd.read_csv("./dalys-rate-from-all-causes.csv")
dayls_days.head(5)
print(dayls_days)