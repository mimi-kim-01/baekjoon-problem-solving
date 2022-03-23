import sys

S1, S2, S3 = map(int, sys.stdin.readline().split())
sum_list = []
max_list = []

for i in range(1, S1 + 1):
    for j in range(1, S2 + 1):
        for k in range(1, S3 + 1):
            sum_list.append(i + j + k)

max_list = [i for i in sum_list if sum_list.count(i) == max(sum_list, key = sum_list.count)]
max_list = list(set(max_list))
max_list.sort()

print(max_list[0])