"""
이게 백준 1450번 풀이인데, 도저히 못풀어먹겠다.
"""

import sys

n, s = list(map(int, sys.stdin.readline().split()))
ws = list(map(int, sys.stdin.readline().split()))

ws = sorted(ws, reverse=True)


def solve(size, i):
    if size < 0:
        return 0
    if size == 0:
        return 1
    if sum(ws[i:]) <= size:
        return 2**(n-i)
    return solve(size-ws[i], i+1)+solve(size, i+1)


print(solve(s, 0))
