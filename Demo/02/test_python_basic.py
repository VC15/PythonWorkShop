#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# print and comment
print("Hello World")
# print("大家好！")
""" 多行注释
单行注释用#
多行注释用三个"开始及结束
"""

####################################################
# 1. Primitive Datatypes and Operators
####################################################
print('(1 + 1) * 10 - 4 / 2 = ', (1 + 1) * 10 - 4 / 2) # Math
print('Pay Attention: 5 / 2 = ', 5 / 2, ', 5.0 / 2 = ',  5.0 / 2, ' and 5 // 2 = ', 5 // 2) # normal division and floored division
print('Another : 5 / 2 = %.2f, 5.0 / 2 = %.2f and 5 // 2 = %.2f (in fact is %d)' % (5 / 2,  5.0 / 2, 5 // 2, 5 // 2)) # print format
print("7 % 3 = {0} and 2 ** 4 = {1}".format(7 % 3, 2 **4))# Modulo operation and exponentiation
print('True and False =>', True and False) # Boolean Operators
print('False or True =>', False or True)

####################################################
# 2. Variables and Collections
####################################################
# Strings
str1 = "Practice"
str2 = ' is'
str3 = ' important!\n'
str = str1 + str2 + str3
print(str * 3)

# Lists store sequences
li = [1, 2, 3]
print('li[0] = {} and li[2] = {}'.format(li[0], li[2])) # Start from 0

dict = {'Name': 'Explore', 'Age': 7, 'Class': 'First'}
print('{} is {} year old and is the {} class'.format(dict['Name'], dict['Age'], dict['Class']))

# input Variable
number = int(input("Please input a number: "))
print("The input number is ", number)

####################################################
#  3. Control Flow
####################################################
# If and ELSE
if number > 5:
    print("The input number is larger than 5.")
elif number < 4:
    print("The input number is smaller than 4.")
else:
    print("The input number is actually 4.")

# For Loop
number2 = number // 5 + 1
for i in range(number2):
    print(i)

####################################################
#  4. Function
####################################################
def add_five(x):
    return x + 5

print("Input number + 5 = ", add_five(number))
