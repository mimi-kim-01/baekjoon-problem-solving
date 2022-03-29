def pelindrome(num, len):
    if len%2 == 0:
        for i in range(int(len/2)):
            if (num[i] != num[len - 1 - i]): return 0
    else:
        for i in range(int(len/2)):
            if (num[i] != num[len -1 -i]): return 0
    return 11

while True:
    num = input()
    if (num == '0'): break
    num_len = len(num)
    result = pelindrome(num, num_len)
    if result == 0: print("no")
    else: print("yes")
