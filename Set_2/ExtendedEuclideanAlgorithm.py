import random

def ExtendedEuclideanAlgorithm(a:int, b:int) -> tuple[int, int, int]:
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q = b//a 
        r = b%a
        m, n = x-u*q, y-v*q
        b,a = a,r
        x,y = u,v
        u,v = m,n
    mcd = b
    return mcd, x, y

def main():
    print(ExtendedEuclideanAlgorithm(41545998005971238876458051627852835754086854813200489396433, \
               88414116534670744329474491095339301121066308755769402836577))
if __name__ == "__main__":
    main()