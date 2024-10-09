#!/usr/bin/python3

def canUnlockAll(boxes):
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
