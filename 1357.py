def Rev(num):
    digit = []; new = 0
    digit = list(map(int, str(num)))
    cnt = 0
    for i in digit:
        new += i*(10**cnt)
        cnt += 1
    return new

X, Y = map(str, input().split())

print(Rev(Rev(X) + Rev(Y)))