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
    start = time.time()
    return pow(m, e, n),time.time()-start

def crypt_crt(m: int, p: int, q: int,e:int) -> int:
    Sp = pow(m, e, p)
    Sq = pow(m, e, q)
    n = p * q
    start = time.time()
    return (q* pow(q,-1,p) *Sp+ p*pow(p,-1,q)*Sq) % (n),time.time()-start

def decrypt(c: int, d: int, n: int) -> int:
    return pow(c, d, n)

def main():
    base = []
    crt = []
    public, private,primes = rsa_keygen()
    for _ in range(100):
        m = np.random.randint(2**61, 2**62)
        c,time_base = crypt(m, public[0], public[1])
        d,time_crt = crypt_crt(m, primes[0], primes[1],public[0])
        base.append(time_base)
        crt.append(time_crt)

    print("Base: ",np.mean(base))
    print("CRT:  ",np.mean(crt))
    # print('Encrypted message: ', c)
    # print('Encrypted message: ', d)
    # m = decrypt(c, private[0], private[1])
    # print('Decrypted message: ', m)
    # m = decrypt(d, private[0], private[1])
    # print('Decrypted message: ', m)

if __name__ == '__main__':
    main()