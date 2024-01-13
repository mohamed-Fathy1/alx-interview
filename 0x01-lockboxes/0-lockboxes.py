#!/usr/bin/python3
'''
    Script that determines if all the boxes can be opened.
'''


def canUnlockAll(boxes):
    '''
       Method that determines if all the boxes can be opened.
       @boxes: list of lists
    '''

    res_dct = {i: False for i in range(len(boxes))}
    res_dct[0] = True

    missedIndex = 1
    loopAgain = True
    while (loopAgain):
        keys = boxes[0]
        loopAgain = False
        missingKeys = False
        for i in range(missedIndex, len(boxes)):
            if res_dct[i]:
                keys += boxes[i]
                continue

            if i not in keys:
                missingKeys = True
                if loopAgain is False:
                    missedIndex = i
                continue

            keys += boxes[i]
            res_dct[i] = True
            if missingKeys:
                loopAgain = True

    isUnlockble = all(lock is True for lock in list(res_dct.values()))
    return isUnlockble
