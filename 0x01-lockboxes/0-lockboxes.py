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
        - You are given n boxes numbered from 0 to n-1.
        - Each box can contain keys to other boxes.
        - The first box (boxes[0]) is always unlocked.
        - A key with the same number as a box opens that box.
        - The goal is to determine if all boxes can be unlocked
        using the keys inside.
    """
    n = len(boxes)

    unlocked = [False] * n
    unlocked[0] = True

    keys = boxes[0]

    stack = keys[:]

    while stack:
        current_key = stack.pop()

        if current_key < n and not unlocked[current_key]:
            unlocked[current_key] = True
            stack.extend(boxes[current_key])

    return all(unlocked)
