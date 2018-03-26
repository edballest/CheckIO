# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 13:19:30 2017

@author: Master
"""

def checkio(first,second):
    first_list=first.split(',')
    second_list=second.split(',')
    common_list=[]
    for word in first_list:
        if word in second_list:
            common_list.append(word)
    
    common_list.sort()
    return ','.join(common_list)
