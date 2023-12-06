#!/usr/bin/python3
"""the pascal_traigle module"""


def pascal_triangle(x):
    """pascal traigle body class"""
    if x <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != x:
        trgl = triangles[-1]
        tmp = [1]
        for t in range(len(trgl) - 1):
            tmp.append(trgl[t] + trgl[t + 1])
        tmp.append(1)
        triangles.append(tmp)
    return
