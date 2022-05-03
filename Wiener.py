import gmpy2


# 展开为连分数
def continuedFra(x, y):
    cF = []
    while y:
        q, r = gmpy2.f_divmod(x, y)
        cF += [q]
        x, y = y, r
    return cF


def Simplify(ctnf):
    numerator = 0
    denominator = 1
    for x in ctnf:
        numerator, denominator = denominator, gmpy2.mul(
            x, denominator) + numerator
    return numerator, denominator


# 连分数化简
def calculateFrac(x, y):
    cF = continuedFra(x, y)
    cF = map(Simplify, [cF[0:i] for i in range(1, len(cF))])
    return list(cF)


# 解韦达定理
def solve_pq(a, b, c):
    par = gmpy2.isqrt(gmpy2.mul(b, b) - gmpy2.mul(4, c))
    return gmpy2.div(-b + par, 2), gmpy2.div(-b - par, 2)


def wienerAttack(e, n):
    for d, k in calculateFrac(e, n):
        if k == 0:
            print("k is 0")
            continue
        q, r = gmpy2.f_divmod((gmpy2.mul(e, d) - 1), k)
        if r != 0:
            print("r is not 0")
            continue
        phi = q
        p, q = solve_pq(1, n - phi + 1, n)
        if gmpy2.mul(p, q) == n:
            return d
    print('not find!')
