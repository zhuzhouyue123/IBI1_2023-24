#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   IBI1_student_database.py
@Time    :   2024/05/10 23:43:28
@Author  :   Zhu Zhouyue 
@Version :   1.0
@Contact :   zhouyue.23@intl.zju.edu.cn
@Desc    :   None
'''

# here put the import lib

# class
class IBI1_student():
    def __init__(self, name:str, major:str, portfolio:int, group_project:int, exam:int) -> None:
        self.name = name
        self. major = major
        self.portfolio = portfolio
        self.group_project = group_project
        self.exam = exam
    
    def details(self):
        print(f"Name: {self.name} Major: {self.major} Portfolio Score: {self.portfolio} Group Project: {self.group_project} Exam Score: {self.exam}")

student = IBI1_student("Rob", "BMI", 100, 90, 80)
student.details()