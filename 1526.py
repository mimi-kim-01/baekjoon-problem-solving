def number(N):
    num = N
    while True:
        sign = 1
        for i in str(num):
            if i != '4' and i != '7': 
                num -= 1
                sign = 0
                break
        if sign == 1: return num

N = int(input())

print(number(N))