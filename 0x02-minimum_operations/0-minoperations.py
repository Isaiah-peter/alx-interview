#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """
    return n is impossible to achieve, returns 0
    """
    if not isinstance(n, int):
        return 0

    operations = 0
    iterator = 2
    while (iterator <= n):
        if not (n % iterator):
            n = int(n / iterator)
            operations += iterator
            iterator = 1
        iterator += 1
    return operations