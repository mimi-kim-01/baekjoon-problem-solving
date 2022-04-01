import sys

counts = [0] * 26

sentence = sys.stdin.read()

for i in range(26):
    counts[i] = sentence.count(chr(i+97))

maxcnt = max(counts)
for i in range(26):
    if counts[i] == maxcnt: print(chr(i+97), end = '')