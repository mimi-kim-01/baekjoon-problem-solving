import sys

N, m, M, T, R = map(int, sys.stdin.readline().split())
original = m
do = 0
time = 0

while do < N:
    if original + T > M:
        break
    if m + T <= M:
        m += T
        do += 1
    else: 
        m -= R
        if m < original:
            m = original
    time += 1

print(time if do == N else -1)