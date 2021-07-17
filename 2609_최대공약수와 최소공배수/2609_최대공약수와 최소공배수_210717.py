def gcd(a, b):
    if b == 0:
        return a
    else:
        return(gcd(b, a % b))


A, B = map(int, input().split())

gcd_AB = gcd(A, B)
print(gcd_AB)
print((A * B) // gcd_AB)
