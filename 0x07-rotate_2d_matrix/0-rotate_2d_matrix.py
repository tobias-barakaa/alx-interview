#!/usr/bin/python3
"""Rotate in 2D
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in-place.

    :param matrix: The input 2D matrix to be rotated.
    :type matrix: List[List[int]]
    """
    def rotate_2d_matrix(matrix):
        """
        Rotates a 2D matrix 90 degrees clockwise.
        """
        return list(zip(*matrix[::-1]))
