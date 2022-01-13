N, M = map(int, input().split())

print( abs(((N-1) // 4) - ((M-1) // 4)) + abs(((N-1) % 4) - ((M-1) % 4)) )