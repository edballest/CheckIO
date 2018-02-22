# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 00:28:29 2018

@author: Eduardo
"""

def check_grid(grid):
    try:
        previousFirst = 'A' #assure its different from the first
        for l in grid:
            assert not(l[0] == previousFirst)
            for i in range(len(l)-1):
                e1 = l[i]
                e2 = l[i+1]
                assert not(e1 == e2)
            previousFirst = l[0]
            
        return True
    except AssertionError:
        return False
    
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_grid([["X", "Z"], ["Z", "X"]]), "2x2 Good"
    assert check_grid([["X", "Z", "X"],
                       ["Z", "X", "Z"],
                       ["X", "Z", "X"]]), "3x3 Good"
    assert check_grid([["X", "Z", "X", "Z"],
                       ["Z", "X", "Z", "X"]]), "2x4 Good"
    assert not check_grid([["X", "X"],
                           ["X", "X"]]), "2x2 Bad"
    assert not check_grid([["X", "Z", "X"],
                           ["Z", "Z", "Z"],
                           ["X", "Z", "X"]]), "3x3 Bad"
    assert not check_grid([["X", "Z", "X", "Z"],
                           ["X", "Z", "X", "Z"]]), "2x4 Bad"
