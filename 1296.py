def winning_rate(word):
    word += name
    L = word.count('L')
    O = word.count('O')
    V = word.count('V')
    E = word.count('E')
    rate = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    print(rate)
    return rate

name = input()
words = []; rates = []
T = int(input())
for i in range(T):
    a = input()
    words.append(a)
words.sort() #to alphabetical order
print(words)
for i in range(len(words)):
    rates.append(winning_rate(words[i]))
maxrate = max(rates)
for i in range(len(rates)):
    if rates[i] == maxrate:
        print(words[i])
        break