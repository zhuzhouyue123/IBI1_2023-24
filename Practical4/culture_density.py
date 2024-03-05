#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   culture_density.py
@Time    :   2024/03/05 13:40:02
@Author  :   Zhu Zhouyue 
@Version :   1.0
@Contact :   zhouyue.23@intl.zju.edu.cn
@Desc    :   None
'''

# here put the import lib

# Pseudocode
'''
The first day:
density << 5
day_counter << 1
Create a while loop
In each loop
density << 2*density
day_counter += 1
When density > 90, exit the loop.
Print out current density & day_counter.
''' 

density = 5  # Variables assignment
day_counter = 1
while density < 90: # for loop
    density = 2 * density
    day_counter += 1
    # print(density)  # for test
    # print(day_counter)  # for test
print("At the day", str(day_counter), "the cell density goes over 90%.")