H, M = map(int, input().split(' '))


time = 24 * 60 + 60 * H + M - 45


print(time // 60 % 24, time % 60)
