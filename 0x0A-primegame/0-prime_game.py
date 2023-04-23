#!/usr/bin/python3
"""0x0A. Prime Game
"""


def findPrimes(num):
    """Returns list of primes up to parameter value n, in ascending order.
    Return:
        primes (list) of (int): list of primes to n, or
        (None): on failure

    """

    if (type(num) is not int or num < 0):
        return None
    primeNum = []
    for candidate in range(2, num + 1):
        prime = True
        for divisor in range(2, candidate):
            if (candidate % divisor == 0):
                prime = False
                break
        if (prime):
            primeNum.append(candidate)
    return primeNum


def isWinner(x, nums):
    """Simulates a game of primes between Ben and Maria, returns the winner.
    Return:
        (str): name of the player that won the most rounds, or
        (None): on failure or no winner found

    """
    if (type(nums) is not list or not all([type(n) is int for n in nums]) or
            not all([n > -1 for n in nums])):
        return None

    if (type(x) is not int or x != len(nums)):
        return None

    nums.sort()
    primes = findPrimes(nums[-1])
    if (primes is None):
        return None

    Maria = 0
    Ben = 0
    for n in nums:
        prime_ct = 0
        for prime in primes:
            if (prime <= n):
                prime_ct += 1
            else:
                break
        if prime_ct % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if (Maria > Ben):
        return "Maria"
    elif (Ben > Maria):
        return "Ben"
    else:
        return None
