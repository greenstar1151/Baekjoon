import sys

N = int(input())
k = int(input())

lower = 1
upper = N
mid = (lower + upper) // 2
is_close = False

def count_under_mid(n, N): # 1번 열부터 순회하며 n ** 2 이하의 수의 개수를 세기
    counter = 1 # n행 n열의 숫자 1개 더하기
    for i in range(1, n):
        if i * N <= n ** 2: # i열 N행이 n ** 2 보다 작다면 (i행 || i열)의 숫자들은 n ** 2 이하임이 보장
            counter += 2 * (N - (i - 1)) - 1
        else: # 그렇지 않다면 i열에서 n ** 2 이하의 숫자들만 세기
            counter += 2 * ((n ** 2 // i) - (i - 1)) - 1 
    return counter

if k == 1: # k == 1일때는 항상 1
    print(1)
    sys.exit(0)
else:
    while True: # 제곱수들을 기준으로 이분탐색, [n ** 2 이하의 수의 개수] < k <= [(n+1) ** 2 이하의 수의 개수]를 만족하는 n 값을 찾기
        under_count = count_under_mid(mid, N)
        if under_count < k:
            lower = mid
            mid = (lower + upper) // 2
        else:
            upper = mid
            mid = (lower + upper) // 2

        if under_count < k and lower == mid:
            break
    
#print(under_count, lower, mid, upper)

middle_numbers = []
for r in range(1, mid + 1): # 위에서 찾은 n ** 2 와 (n+1) ** 2 사이의 모든 수를 리스트로 내보내기 (1번 열부터 순회하며)
    if r * N < mid ** 2: # r열 N행이 n ** 2 보다 작다면 (r행 || r열)의 숫자들은 위 조건에 해당되지 않음
        continue
    else: # 임의의 r열은 range(r, r * N + 1, r)의 형식이므로 n ** 2 < x <= (n+1) ** 2 을 만족하는 모든 x는 아래의 코드로 추출 가능
        middle_numbers += list(range((mid ** 2 // r) * r + r, min(r * N + 1, (mid + 1) ** 2 + 1), r)) * 2 # 배열 A가 대칭행렬이므로 * 2
        middle_numbers += [(mid + 1) ** 2] # 제곱수 더해주기

middle_numbers.sort() # 정렬(배열 B - 오름차순)
#print(middle_numbers)
print(middle_numbers[k - under_count - 1]) # k에서 [n ** 2 이하의 수의 개수]를 빼주고 B의 인덱스는 1부터 시작하므로 1을 뺌



'''
[1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
[2,  4,  6,  8,  10, 12, 14, 16, 18, 20]
[3,  6,  9,  12, 15, 18, 21, 24, 27, 30]
[4,  8,  12, 16, 20, 24, 28, 32, 36, 40]
[5,  10, 15, 20, 25, 30, 35, 40, 45, 50]
[6,  12, 18, 24, 30, 36, 42, 48, 54, 60]
[7,  14, 21, 28, 35, 42, 49, 56, 63, 70]
[8,  16, 24, 32, 40, 48, 56, 64, 72, 80]
[9,  18, 27, 36, 45, 54, 63, 72, 81, 90]
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
'''
