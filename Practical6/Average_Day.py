#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Average_Day.py
@Time    :   2024/03/19 13:19:12
@Author  :   Zhu Zhouyue 
@Version :   1.0
@Contact :   zhouyue.23@intl.zju.edu.cn
@Desc    :   None
'''

# This program can generate a pie figure that include the students' average time (hours) of activities.

# here put the import lib
import matplotlib.pyplot as plt

# functions
def dict_to_pie(dict):   # define a function that can generate a figure.
    plt.pie(dict.values(),   # pie plot
            labels=dict.keys(), 
            colors=["#BFDFD2", "#257d8b", "#68bed9", "#efce87", "#eaa558", "#ed8d5a"],
            autopct="%1.1f%%")
    plt.title("Average Day")  # set the title
    # plt.legend(loc="upper left", bbox_to_anchor=(1,1))   # show the legend
    plt.show() # show the img
    plt.clf() # close the figure

# main
day = {"Sleeping": 8, "Classes": 6, "Studying": 3.5, "TV": 2, "Music": 1}   # assign the dictionary to store the data
other = 24 - day["Sleeping"] - day["Classes"] - day["Studying"] - day["TV"] - day["Music"]  # calculate the time of other
day["Other"] = other  # add a key:value of other time
dict_to_pie(day) # draw the figure
