from sympy.ntheory.modular import crt
import gmpy2
import owiener
import random
import multiprocessing


def load_data(datanum):
    with open(file="./test/data%d" % (datanum), mode='r') as file:
        n, e, c = file.read(256), file.read(256), file.read(256)
        n, e, c = int(n, 16), int(e, 16), int(c, 16)
        return n, e, c


def func(x, c, n):
    return (x * x + c) % n


def Pollard_Rho(n):
    # 使用 https://xz.aliyun.com/t/6703 中的改进算法
    # 得到 n 的一个因子
    if n == 4:
        return 2
    cnt=0
    while (1):
        cnt+=1
        if cnt>1000000:
            break
        c = random.randrange(2, n - 1)
        t = gmpy2.mpz(0)
        r = gmpy2.mpz(0)
        p = gmpy2.mpz(1)
        q = gmpy2.mpz(1)
        while (1):
            for i in range(100):
                t = func(t, c, n)
                r = func(func(r, c, n), c, n)
                if (t == r):
                    break
                else:
                    q = p * abs(t - r) % n
                    if (q == 0):
                        break
                p = q
            d = gmpy2.gcd(p, n)
            if (d > 1):
                return d
            if (t == r):
                break
        return 0


def task(num):

    n, e, c = load_data(num)
    n = gmpy2.mpz(n)
    e = gmpy2.mpz(e)
    c = gmpy2.mpz(c)

    # 得到 p, q
    p = Pollard_Rho(n)
    if p==0:
        return 0
    q = n // p

    phi = (p - 1) * (q - 1)

    # 求 e 关于 phi 的逆元
    d = gmpy2.invert(e, phi)
    # 求解密文
    m = gmpy2.powmod(c, d, n)
    print("m = 0x%X" % m)
    return hex(m)


# 多线程
def solve(lst):
    pool = multiprocessing.Pool(processes=len(lst))

    for i in lst:
        pool.apply_async(task, (i, ))

    pool.close()
    pool.join()