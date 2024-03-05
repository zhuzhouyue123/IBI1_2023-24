#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   recursive.py
@Time    :   2024/03/04 16:13:56
@Author  :   Zhu Zhouyue 
@Version :   1.0
@Contact :   zhouyue.23@intl.zju.edu.cn
@Desc    :   None
'''

# here put the import lib

'''
Description:
The first num of the sequence is 4, so assign the variable a_0 to 4.
The next number a_next = 2*a_current + 3
If we want to output five numbers of the sequence. We can use for loops.
'''

a = 4  # assign a_0 first
for i in range(5):  # for loops
    print(a)      # print the a_0 out
    a = 2*a +3    # update value of a