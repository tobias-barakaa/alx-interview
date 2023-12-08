#!/usr/bin/python3

"""
    Determines if all the boxes can be opened.

    Args:
    - boxes (list of lists): A list of lists where each inner list represents a box.
                             Each box may contain keys to other boxes, and a key with the
                             same number as a box can open that box.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.

    Constraints:
    - The first box boxes[0] is assumed to be unlocked.
    - All keys are positive integers.
    - There can be keys that do not have corresponding boxes.
"""


def canUnlockAll(boxes):
    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
