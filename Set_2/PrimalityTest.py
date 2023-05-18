from FastExponential import fast_modular_exponentiation

def rabin_test(n:int)->bool:
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    m = n - 1
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1
    a = 2
    b = fast_modular_exponentiation(a, m, n)
    if b == 1 or b == n-1:
        return True
    for i in range(k-1):
        b = fast_modular_exponentiation(b, 2, n)
        if b == n-1:
            return True
    return False

def main():
    n = int(input())
    print(rabin_test(n))

if __name__ == '__main__':
    main()
