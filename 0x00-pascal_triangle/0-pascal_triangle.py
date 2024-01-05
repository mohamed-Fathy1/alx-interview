#!/usr/bin/python3
'''module'''


def pascal_triangle(n):
    '''pascal_triangle function'''
    tmp = [0, 1, 0]
    result = []

    for i in range(0, n):
        tmp2 = []
        tmp3 = []
        for k in tmp:
            if k != 0:
                tmp3.append(k)
        result.append(tmp3)
        for j in range(len(tmp)):
            if j < len(tmp) - 1:
                tmp2.append(tmp[j] + tmp[j + 1])
        tmp2.append(0)
        tmp2.insert(0, 0)
        tmp = tmp2
    return (result)
