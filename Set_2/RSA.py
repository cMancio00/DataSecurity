from PrimeGenerator import prime_generator
import numpy as np
import time

def rsa_keygen(bit_lenght: int = 1024) -> tuple:
    p = prime_generator(bit_lenght)
    q = prime_generator(bit_lenght)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = pow(e, -1, phi)
    return (e, n), (d, n),(p,q)

def crypt(m: int, e: int, n: int) -> int:
    return pow(m, e, n)

def decrypt(c: int, d: int, n: int) -> int:
    start = time.time()
    return pow(c, d, n),time.time()-start

def decrypt_crt(c:int,d:int,p:int,q:int) -> int:
    Sp = d % (p - 1)
    Sq = d % (q - 1)
    start = time.time()
    q_inv = pow(q, -1, p)
    #p_inv = pow(p, -1, q)
    m1 = pow(c, Sp, p)
    m2 = pow(c, Sq, q)
    h = (q_inv * (m1 - m2)) % p
    return m2 + h * q,time.time()-start


def main():
    base = []
    crt = []
    public, private,primes = rsa_keygen()
    for _ in range(100):
        m = np.random.randint(2**61, 2**62)
        c = crypt(m, public[0], public[1])
        m,time_base = decrypt(c, private[0], private[1])
        m,time_crt = decrypt_crt(c, private[0], primes[0],primes[1])
        base.append(time_base)
        crt.append(time_crt)

    print("Base: ",np.mean(base))
    print("CRT:  ",np.mean(crt))
    print("Percentuale di miglioramento: ",\
          ((np.mean(base)-np.mean(crt))/np.mean(base))*100,"%")




if __name__ == '__main__':
    main()