N = int(input())
curr_pattern = list(input())
for _ in range(N-1):
    line = input()
    for i, c in enumerate(curr_pattern):
        if line[i] != c:
            curr_pattern[i] = '?'

print(''.join(curr_pattern))
