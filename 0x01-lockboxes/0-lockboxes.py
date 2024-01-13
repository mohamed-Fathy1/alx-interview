#!/usr/bin/python3
'''
    Script that determines if all the boxes can be opened.
'''
# from functools import reduce


def canUnlockAll(boxes):
    '''
       Method that determines if all the boxes can be opened.
       @boxes: list of lists
    '''
    isUnlockble = True

    res_dct = {i: False for i in range(len(boxes))}
    res_dct[0] = True

    loopAgain = True
    i = 0
    while (loopAgain and (not isUnlockble or i == 0)):
        keys = boxes[0]
        loopAgain = False
        for i in range(1, len(boxes)):
            # print(keys)
            if res_dct[i]:
                keys += boxes[i]
                continue

            if i not in keys:
                isUnlockble = False
                continue

            keys += boxes[i]
            res_dct[i] = True
            loopAgain = True

    isUnlockble = all(flag is True for flag in list(res_dct.values()))
    return isUnlockble
