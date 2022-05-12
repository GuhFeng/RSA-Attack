from sympy.ntheory.modular import crt
import gmpy2
import owiener
import random
import threading
import multiprocessing

def load_data(datanum):
    with open(file="./test/data%d" % (datanum), mode='r') as file:
        n, e, c = file.read(256), file.read(256), file.read(256)
        n, e, c = int(n, 16), int(e, 16), int(c, 16)
        return n, e, c

def attack1(n, e, c):
    if e > 2:
        return -1
    i = 0
    while 1:
        tmp = gmpy2.iroot(c + i * n, e)
        if tmp[1]:
            return tmp[0]
        else:
            i += 1

def func(x, c, n):
    return (gmpy2.powmod(x, n-1, n) + c) % n

def Pollard_Rho(n, e, c):
    if n==4:
        return 2
    while(1):
        c = random.randrange(2, n-1)
        t = gmpy2.mpz(0)
        r = gmpy2.mpz(0)
        p = gmpy2.mpz(1)
        q = gmpy2.mpz(1)
        while(1):
            for i in range(100):
                t = func(t, c, n)
                r = func(func(r, c, n), c, n)
                if(t == r):
                    break
                else:
                    q = p * abs(t - r) % n
                    if(q == 0):
                        break
                p = q
            d = gmpy2.gcd(p, n)
            if(d>1):
                return d
            if(t == r):
                break;
    
def task(num, p):
    print("test: 3589  %d" % (Pollard_Rho(3589, 1, 1)))
    n, e, c = load_data(num)
    n = gmpy2.mpz(n)
    e = gmpy2.mpz(e)
    c = gmpy2.mpz(c)
    print("case %d: n=%d\ne=%d\nc=%d\n" % (num, n, e, c))
    q = n / p
    q = gmpy2.mpz(q)
    print("p = %d    q = %d" % (p, q))
    if(gmpy2.is_prime(p)):
        print("p is a prime")
    else:
        print("p is not a prime")
    if(gmpy2.is_prime(q)):
        print("q is a prime")
    else:
        print("q is not a prime")
        

s = ""
for i in range(256-5):
    s = s + '0'
s = s + "587F9"
for i in range(256*2):
    s = s + '0'
print(s)

'''
i = 12
p = 920724637201
task(i, p)

case 21: answer: 97
case 21: answer: 37
case 12: answer: 15110322257
case 12: answer: 2383
case 12: answer: 61
case 3: answer: 176953189543913
case 3: answer: 3
case 3: answer: 3
case 3: answer: 3
'''