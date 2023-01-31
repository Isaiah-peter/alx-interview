#!/usr/bin/python3
"""lockbox"""


def join(T, R):
    """join the lock"""
    res = []
    for e in R:
        res += T[e]
    return res


def canUnlockAll(boxes):
    """check can lock"""
    index = 0
    total = list(set(boxes[0]) | {0})
    added = True
    while added:
        added = False
        for j in join(boxes, total[index:]):
            if j not in total:
                total.append(j)
                index += 1
                added = True
    print(total)

    return len(total) == len(boxes)
