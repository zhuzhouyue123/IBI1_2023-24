#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   repetitive_counter.py
@Time    :   2024/05/20 20:11:18
@Author  :   Zhu Zhouyue 
@Version :   1.0
@Contact :   zhouyue.23@intl.zju.edu.cn
@Desc    :   None
'''

# here put the import lib

# variables
seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
patterns = ["GTGTGT", "GTCTGT"]
count = 0

# find patterns
for i in range(0,len(seq)):
    if seq[i:i+6] in patterns:
        count += 1
# print the result
print(count)