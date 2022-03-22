import sys

A, B = map(int, sys.stdin.readline().split())

multiple = []

for i in str(A):
    for j in str(B):
        multiple.append(int(i)*int(j))

print(sum(multiple))