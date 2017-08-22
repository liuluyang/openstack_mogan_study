
def _gcd(m, n):
    if n == 0:
        m, n = n, m
    while m != 0:
        m, n = n%m , m
    return n

print _gcd(18,10)

