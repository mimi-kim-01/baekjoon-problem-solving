def multisep(N):
    sep = 0 
    while sep != len(N) - 1:
        left = 1; right = 1
        for i in range(sep+1):
            left *= N[i]
        for j in range(sep+1, len(N)):
            right *= N[j]
        if left == right: 
            return 1
        sep += 1
    return 0

N = list(input())

for i in range(len(N)):
    N[i] = int(N[i])

if multisep(N) == 1: print("YES")
else: print("NO")