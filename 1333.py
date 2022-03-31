def time(N, L, D):
    for i in range(N):
        for j in range(((L+5)*N)//D + 1):
            if (L+(L+5)*i <= D*j < (L+5)*(i+1)):
                return (D*j)  
    return -1

N, L, D = map(int, input().split())

if time(N, L, D) != -1:
    print(time(N, L, D))
else: print((((L+5)*N)//D)*D)