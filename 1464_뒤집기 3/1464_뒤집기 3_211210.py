from collections import deque


S = input()


result = deque()
result.append(S[0])
# 문자열을 순회하며 새로운 문자열의 마지막 문자보다 앞서면 뒤에, 아니면 앞에 붙이기
# 이것이 가능한 이유는 맨 마지막에 뒤집기를 무조건 한다고 가정하면 사전순 뒤에 오는 문자를 맨 앞으로 보내기
# k번째, k+1번째 뒤집기로: A C A -> A A C (C > A, 3번째 A를 맨 앞으로) / A A C B -> B A A C (C > B, B를 맨 앞으로)
for i in range(1, len(S)):
    if result[-1] < S[i]:
        result.appendleft(S[i])
    else:
        result.append(S[i])
    
print(''.join(map(str, result))[::-1])
