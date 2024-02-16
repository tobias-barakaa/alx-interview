#!/usr/bin/python3
""" 
    Prime Game"""
    

def isWinner(x, nums):
    """ Game"""
    x = 0
    y = 0
    if x == 0 or x == 1:
        return None
    for i in nums:
        if i == 2:
            x += 1
        else:
            y += 1
    if x > y:
        return "Maria"
    if y > x:
        return "Ben"
    return None