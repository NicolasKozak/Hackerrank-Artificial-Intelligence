# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 18:31:29 2022

@author: Nico
"""

import numpy as np
import math

def corr(x, y):
    SS = lambda x,y:(sum([i*j for (i,j) in zip(x,y)])-(sum(x)*sum(y))/len(x))
    try:
        correlation = SS(x, y)/math.sqrt(abs(SS(x,x)*SS(y,y)))
    except:
        correlation = 0
    return correlation

T = int(input())

for i in range(T):
    N = int(input())
    gpa = [float(k) for k in input().split()]
    corrlist = []
    for j in range(5):
        marks = [float(k) for k in input().split()]
        corrlist.append(corr(gpa, marks))
    print(np.argmax(corrlist)+1)     
    