# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 01:24:00 2018

@author: Master
"""

def getExp(number,base,l):
    number=abs(number)
    if number<base:
        return 0
    e=1
    while number//base**e>=base and e<(l-1):
        e+=1
    return e  

def getNumberStr(number,base,exp,decimals):
    n=number/base**exp
    if decimals==0:
        return str(int(n))
    else:
        return ('{:.{prec}f}'.format(round(n,decimals), prec=decimals))
    

def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    l = len(powers)
    e = getExp(number,base,l)
    p = powers[e]
    return getNumberStr(number,base,e,decimals)+p+suffix
    
    
    return str(number)

