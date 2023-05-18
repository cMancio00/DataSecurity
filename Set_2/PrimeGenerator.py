from PrimalityTest import rabin_test
import random

def prime_generator(bit_lenght:int = 1024)->int:
    while True:
        n = random.randrange(2**(bit_lenght-1), 2**bit_lenght)
        if rabin_test(n):
            return n

def main():
    print(prime_generator())

if __name__ == '__main__':
    main()



