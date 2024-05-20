#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Chocolate_bar_affordability_calculator.py
@Time    :   2024/05/10 00:00:17
@Author  :   Zhu Zhouyue 
@Version :   1.0
@Contact :   zhouyue.23@intl.zju.edu.cn
@Desc    :   None
'''

# here put the import lib

# functions
def chocolate_counter(money, price):
    count = money // price
    changes = money % price
    return count, changes

money = 100
price = 7
count, money = chocolate_counter(money, price)
print(f"You can buy {count} bars and changes are {money}$.")