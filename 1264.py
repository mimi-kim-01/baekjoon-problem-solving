while True:
    line = input()
    if line == '#': break
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    cnt = 0
    for letter in line:
        if letter in vowels: cnt += 1
    print(cnt)
