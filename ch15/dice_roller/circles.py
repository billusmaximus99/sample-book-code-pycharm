#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 08:24:05 2020

@author: billemerson
"""
import math


class Circle:
    
    MAX_CIRCLE_SIZE = 1000
    
    @classmethod
    def getMaxCircleArea(cls):
        return math.pi*(cls.MAX_CIRCLE_SIZE**2)
    
    @staticmethod
    def getAnyCircleArea(r):
        return math.pi*(r**2)
    
    
    def __init__(self,r):
        self.radius = r
    
    def getArea(self):
        return math.pi*(self.radius**2)
    
    def getCircumference(self):
        return math.pi*2*self.radius
    
    