# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 00:09:08 2018

@author: Master
"""

from numpy import arctan2,pi,NaN
from math import sqrt
import pandas as pd

class Point(object):
    def __init__(self,l,i=NaN):
        self.x = l[0]
        self.y = l[1]
        self.index = i
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getIndex(self):
        return self.index
    def toList(self):
        return (self.getX(),self.getY())
    def angleTo(self,p):
        '''clockwise angle in degrees'''
        x2 = p.getX()-self.getX() #coordinates of p with respect to self
        x1 = p.getY()-self.getY()
        d = (arctan2(x1,x2)*360/(2*pi))
        return (-d+90) %360 # %360 to achieve range 0-360
    def distanceTo(self,p):
        '''Euclidean distance between self and p'''
        dx = p.getX()-self.getX()
        dy = p.getY()-self.getY()
        return sqrt(dx**2+dy**2)
    def __repr__(self):
        return str((self.getX(),self.getY()))
    
class Hull(object):
    def __init__(self,allPoints):
        self.allPoints = allPoints
        self.hullPoints = []
        self.lastAngle = -1 #to make sure first is bigger
        self.setP0()
        self.hullPoints += [self.p0]
        self.setP1(self.getP0()) #P1 is last point added to the hull
        self.AddPoints() 
        while not (self.hullPoints[-1] == self.p0):
            self.setP1(self.hullPoints[-1])
            self.AddPoints()
        self.hullPoints = self.hullPoints[:-1] #erase last p0
    def setP0(self):
        ''' bottom leftmost point'''
        self.p0 = sorted(self.allPoints,key=lambda p: (p.getX(), p.getY()))[0]
    def setP1(self,p1):
        '''p1 Point'''
        self.p1 = p1
    def setLastAngle(self,lastAngle):
        self.lastAngle = lastAngle
    def getP0(self):
        return self.p0
    def getP1(self):
        return self.p1
    def getLastAngle(self):
        return self.lastAngle
    def getHull(self):
        return self.hullPoints
    def getHullIndexes(self):
        indexes = []
        for p in self.hullPoints:
            indexes.append(p.getIndex())
        return indexes
    def AddPoints(self):
        '''Adds the points of a side of the hull'''
        otherPoints = self.allPoints.copy()
        otherPoints.remove(self.p1)
        df = pd.DataFrame(otherPoints, columns = ['Points'])
        df['Angle'] = df['Points'].apply(self.p1.angleTo) #only angle bigger than the last
        df['Distance'] = df['Points'].apply(self.p1.distanceTo)
        df = df[df['Angle']>self.lastAngle]
        df = df.sort_values(by = ['Angle','Distance']) #sorted first by angle then by distance to p1
        df = df[df['Angle'] == min(df['Angle'])] #only the ones with the less angle
        self.hullPoints += list(df['Points'])
        self.lastAngle = list(df['Angle'])[0]
    
def readData(data):
    allPoints = []
    i = 0
    for d in data:
        allPoints.append(Point(d,i))
        i += 1
    return allPoints

def checkio(data):
    
    allPoints = readData(data)
    H = Hull(allPoints)
    return H.getHullIndexes()
