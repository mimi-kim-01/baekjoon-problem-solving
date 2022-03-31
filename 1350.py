N = int(input())
cnt = 0
a = list(map(int, input().split()))
cluster = int(input())
for i in range(N):
    if a[i] != 0 and a[i]%cluster != 0: cnt += 1 + a[i]//cluster
    elif a[i] != 0 and a[i]%cluster == 0: cnt += a[i]//cluster
print(cnt*cluster)