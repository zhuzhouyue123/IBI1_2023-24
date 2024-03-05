#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   variables.py
@Time    :   2024/03/04 14:48:13
@Author  :   Zhu Zhouyue 
@Version :   1.0
@Contact :   zhouyue.23@intl.zju.edu.cn
@Desc    :   None
'''

# here put the import lib


# Practical3 
# Simple math answers
'''
40 >> a  Before the training
36 >> b  After the 1st month
30 >> c  After the 2nd month
abs(a-b) >> d  define the difference between a&b
abs(b-c) >> e  define the difference between b&c
compare d&e
'''
print("Comparison result:")
a = 40
b = 36 # Init the variables
c = 30
d = abs(a-b)
e = abs(b-c)
if d > e: # If statement to judge wether d is bigger than e
    print("d is greater, and the first training regime is better.")
elif d == e:
    print('d & e are same, two training has the same influence.')
else:
    print("e is greater, and the second training regime is better.")

# Results: e is greater, and the second training regime is better.                                                             

print("Truth table of the 'either or:'")

# Either or
# Output truth table
print("X\tY\teither X or Y")
print('-' * 30)
for x in [True, False]:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    for y in [True, False]:
        W = x ^ y  # I think 'either or' is just a 'exclusive or' (xor)
        O = (x or y) and not(x and y) # If I do not use bitwise operators
        print(str(x)+'\t'+ str(y) +'\t'+ str(O))

#Outputs are like this
'''
X	Y	either X or Y
True	True	False
True	False	True
False	True	True
False	False	False
'''

