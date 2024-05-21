#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Favourite_James_Bond.py
@Time    :   2024/05/10 23:32:15
@Author  :   Zhu Zhouyue 
@Version :   1.0
@Contact :   zhouyue.23@intl.zju.edu.cn
@Desc    :   None
'''

# here put the import lib
def find_favorite_bond_actor(birth_year):
    bond_actors = { # the dict contain the name and the year interval
        "Roger Moore": (1973, 1986),
        "Timothy Dalton": (1987, 1994),
        "Pierce Brosnan": (1995, 2005),
        "Daniel Craig": (2006, 2021)
    }
    
    age_18_year = birth_year + 18
    
    for actor, (start_year, end_year) in bond_actors.items():
        if start_year <= age_18_year <= end_year:
            return actor
    
    return "Unknown"

# main
favorite_bond_actor = find_favorite_bond_actor(1980)
print(f"Your favorite James Bond actor is: {favorite_bond_actor}")