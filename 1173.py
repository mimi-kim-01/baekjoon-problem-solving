import sys

N, m, M, T, R = map(int, sys.stdin.readline().split())
original = m
do = 0
rest = 0

while do < N:
    if m + T <= M:
        m += T
        do += 1
    else: 
        m -= R
        rest += 1
        if m < original:
            m = original
    if do == N:
        break

print(do + rest)