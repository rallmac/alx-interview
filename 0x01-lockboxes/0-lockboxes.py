#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of lists): A list of n boxes, where each
        box contains a list
        of keys (represented by integers) to unlock other boxes.

    Returns:
        bool: True if all boxes can be opened, otherwise False.

    Description:
        - You are given a number of boxes
        - Each box can contain keys to other boxes.
        - The first box is always unlocked.
        - A key with the same number as a box opens that box.
        - The goal is to determine if all boxes can be unlocked
        using the keys inside.
    """
    open = set([0])
    closed = set(boxes[0]).difference(open)

    while len(closed) > 0:
        key = closed.pop()

    if key not in open:
        open.add(key)
        closed = closed.union(boxes[key]).difference(open)

    return len(open) == len(boxes)
