#!/usr/bin/python3
"""
    Given a number n, write a method that calculates the fewest number of
    operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
        Method that calculates the fewest number of operations
        needed to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    numOp = 0
    i = 2

    # print('H')

    while i <= n:
        if n % i == 0:
            numOp += i
            n = n / i
        else:
            i += 1

        # print('H' * i)

    return numOp
    # strOp = 'H'
    # pasteStr = ''
    #
    # def copyAll():
    #     '''
    #        returns the string copied
    #     '''
    #     return strOp
    #
    # def paste():
    #     '''
    #         returns the string pasted
    #     '''
    #     return pasteStr
    #
    # if n < 2:
    #     return 0
    # pasteStr = copyAll()
    # strOp += paste()
    # numOfOp = 2
    #
    # while len(strOp) < n:
    #     if len(strOp) % 2 == 0 or len(strOp) == n - 1:
    #         strOp += paste()
    #         numOfOp += 1
    #     elif (len(strOp) * 2) < n:
    #         pasteStr = copyAll()
    #         strOp += paste()
    #         numOfOp += 2
    #     else:
    #         strOp += paste()
    #         numOfOp += 1
    #
    # return numOfOp
