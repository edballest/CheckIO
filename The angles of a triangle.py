# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 21:14:46 2018

@author: Master
"""

import numpy as np

def rad2deg(r):
    return (r*180/np.pi)

def getOppositeAngle(a,b,c):
    '''uses cosine theorem to fin angle oposite of a'''
    rad = np.arccos((b**2+c**2-a**2)/(2*b*c))
    return rad2deg(rad)

def checkio(a, b, c):
    
    (a,b,c)=sorted((a,b,c),reverse=True)
    if a>=b+c:
        return [0, 0, 0]
    
    A=round(getOppositeAngle(a,b,c))
    B=round(getOppositeAngle(b,a,c))
    C=180-A-B
    return [C,B,A]

    