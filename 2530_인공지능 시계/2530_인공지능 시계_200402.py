A, B, C = map(int, input().split())
D = int(input())

sec_total = A * 3600 + B * 60 + C + D

print((sec_total // 3600) % 24, (sec_total // 60) % 60, sec_total % 60)