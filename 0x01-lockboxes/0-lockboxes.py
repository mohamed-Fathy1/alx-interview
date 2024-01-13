#!/usr/bin/python3

# from functools import reduce


def canUnlockAll(boxes):
    isUnlockble = True
    # list = reduce(lambda acc, arr: acc + arr, boxes)
    # for i in range(1, len(boxes)):
    #     print(i)
    #     if i not in list:
    #         isUnlockble = False

    res_dct = {i: False for i in range(len(boxes))}
    res_dct[0] = True
    # print(list(res_dct.values()))

    loopAgain = True
    i = 0
    while (loopAgain and (not isUnlockble or i == 0)):
        # print('loop again \n')
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
        # print("\n\n\n")

    # print(res_dct)

    isUnlockble = all(flag is True for flag in list(res_dct.values()))
    return isUnlockble
