#!/usr/bin/python3
"""
Given a number n, write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Method that calculates the fewest number of operations needed to result in
    exactly n H characters in the file.
    """
    strOp = 'H'
    pasteStr = None

    def copyAll():
        return strOp

    def paste():
        return pasteStr

    if n < 2:
        return 0
    pasteStr = copyAll()
    strOp += paste()
    numOfOp = 2

    while len(strOp) < n:
        if len(strOp) % 2 == 0 or len(strOp) == n - 1:
            strOp += paste()
            numOfOp += 1
        elif (len(strOp) * 2) < n:
            pasteStr = copyAll()
            strOp += paste()
            numOfOp += 2
        else:
            strOp += paste()
            numOfOp += 1

    return numOfOp
