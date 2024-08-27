#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 08:36:14 2020

@author: billemerson
"""

from ch15.dice_roller.circles import Circle


c1 = Circle(4)


print (c1.getArea())

print(Circle.getMaxCircleArea())

print(Circle.getAnyCircleArea(5))

print(Circle.MAX_CIRCLE_SIZE)

c1.newVar = 10

print(c1.newVar)