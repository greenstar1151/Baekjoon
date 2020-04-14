T = int(input())

for _ in range(T):
    case = input()
    Ocount = 0
    score = 0
    for s in case:
        if s == 'O':
            Ocount += 1
            score += Ocount
        elif s == 'X':
            Ocount = 0
    print(score)
