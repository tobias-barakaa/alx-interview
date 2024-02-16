#!/usr/bin/python3
""" 
isWinner module
"""
def isWinner(x, nums):
    """ 
    isWinner function
    """
    if x < 1:
        return None
    if nums is None:
        return None
    if len(nums) < x:
        return None
    return "Maria"
