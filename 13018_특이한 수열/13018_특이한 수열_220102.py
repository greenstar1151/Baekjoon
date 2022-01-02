n, k = map(int, input().split())

if n - k == 0:
    print('Impossible')
else:
    shift_len = n - k
    if shift_len == 1: # k가 n-1개일 경우 수열 A를 1 ~ n으로 만들면 gcd(1, A[1]) == 1 이고 나머지는 모두 1보다 크므로(자기자신) 조건 만족
        shifted_sequence = list(range(1, n+1))
    else: # 수열 A의 앞부분 중 n - k개를 1씩 offset을 주면 gcd(i, A[i]) == gcd(i, i+1) == 1 이고 나머지 뒷부분 k개는 gcd(i, i) == i로 조건 만족
        shifted_sequence = [shift_len] + list(range(1, shift_len)) + list(range(shift_len+1, n+1))
    print(' '.join(map(str, shifted_sequence)))
'''
1 0
1

1 1
X

2 0
2 1

2 1
1 2

2 2
X

3 0
3 1 2

3 1
2 1 3

3 2
1 2 3

3 3
X

4 0
4 1 2 3

4 1
3 1 2 4

4 2
2 1 3 4

4 3
1 2 3 4

4 4
X
'''