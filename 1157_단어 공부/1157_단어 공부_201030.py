word = input()


alphabets = [0] * 26
for c in word:
    if ord(c) <= 90:
        alphabets[ord(c) - 65] += 1
    else:
        alphabets[ord(c) - 97] += 1


most = max(alphabets)
if alphabets.count(most) > 1:
    print('?')
else:
    print(chr(alphabets.index(most) + 65))
