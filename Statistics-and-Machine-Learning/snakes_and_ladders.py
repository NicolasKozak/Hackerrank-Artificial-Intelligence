# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 17:12:45 2022

@author: Nico
"""

import random

T = int(input())
for i in range(T):
    prob = [float(j) for j in input().split(',')]
    lad,snk = [int(j) for j in input().split(',')]
    
    vals = input().split()
    lads = {}
    for j in vals:
        start,end = [int(k) for k in j.split(',')]
        lads[start] = end
        
    vals = input().split()
    snks = {}
    for j in vals:
        start,end = [int(k) for k in j.split(',')]
        snks[start] = end
        
    totalCount = 0
    totalSum = 0
    for j in range(5000):
        pos = 1
        count = 0
        while count < 1000:
            m = random.uniform(0,1)
            move = 0
            if m < prob[0]:
                move = 1
            elif m < prob[0]+prob[1]:
                move = 2
            elif m < prob[0]+prob[1]+prob[2]:
                move = 3
            elif m < prob[0]+prob[1]+prob[2]+prob[3]:
                move = 4
            elif m < prob[0]+prob[1]+prob[2]+prob[3]+prob[4]:
                move = 5
            else:
                move = 6
            if pos+move <= 100:
                pos += move
                if pos in lads:
                    pos = lads[pos]
                elif pos in snks:
                    pos = snks[pos]
            count += 1
            if pos == 100:
                totalCount += 1
                totalSum += count
                break
    print(round(totalSum/totalCount))