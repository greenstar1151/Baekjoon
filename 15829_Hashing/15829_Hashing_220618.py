L = int(input())
string_to_hash = input()

r = 31
M = 1234567891
coefficient = [1]
for _ in range(50):
    coefficient.append(coefficient[-1] * r % M)

H = 0
for i, c in enumerate(string_to_hash):
    H += ((ord(c) - ord('a') + 1) * coefficient[i]) % M
H %= M

print(H)
