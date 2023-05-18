def fast_modular_exponentiation(base:int, exponent:int, modulus:int)->int:
    exponent = bin(exponent)[2:]
    result = 1
    for i in range(0,len(exponent)):
        result = (result * result) % modulus
        if exponent[i] == '1':
            result = (result * base) % modulus
    return result