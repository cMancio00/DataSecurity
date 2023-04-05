from lib.string_preprocessing import number_to_string, sring_to_number
import numpy as np
from numpy import dot,gcd
from numpy.linalg import det
from sympy import mod_inverse,Matrix
import logging
from os.path import exists
from os import mkdir

if not exists("Logs"):
    mkdir("Logs")
logging.basicConfig(format='%(message)s\n', filename='Logs/hill_attack.log',filemode='w', level=logging.INFO)


def calculate_inverse(plaintext:np.ndarray)->np.ndarray:
    denominator = mod_inverse(int(round(det(plaintext),0)),26)
    logging.info("Denominator: {denominator}".format(denominator = denominator))
    inverse = np.zeros(shape = plaintext.shape, dtype = int)
    for i in range(plaintext.shape[0]):
        for j in range(plaintext.shape[1]):
            matrix = np.delete(np.delete(plaintext, j, 0), i, 1)
            determinant = int(round(det(matrix),0))
            inverse[i][j] = (determinant * denominator)
            inverse[i][j] *= (-1)**(i+j)
    return inverse % 26

def check_inverse_exists(plaintext:np.ndarray, block_size:int):
    determinant = int(round(det(plaintext),0))
    logging.info("Determinant: {determinant}".format(determinant = determinant))
    divisor = gcd(determinant, block_size)
    logging.info("Divisor: {divisor}".format(divisor = divisor))
    return divisor == 1

def format_text(text:str,block_size:int,isSniffedChypertext:bool = False)->np.ndarray:
    text = sring_to_number(text)
    if isSniffedChypertext:
        text.resize(int(len(text)/block_size),block_size)
    else:
        text.resize(block_size,block_size)
    text = np.transpose(text)
    return text

def attack(known_cyphertext:np.ndarray, sniffed_plaintext:np.ndarray, block_size:int)->np.ndarray:
    if not check_inverse_exists(sniffed_plaintext, block_size):
        raise ValueError("Inverse does not exist")
    inverse = calculate_inverse(sniffed_plaintext)
    logging.info("Inverse: \n{inverse}".format(inverse = inverse))
    key = dot(known_cyphertext,inverse) % 26
    logging.info("Key: \n{key}".format(key = key))
    return key

def decrypt(founded_key:np.ndarray,sniffed_cyphertext:np.ndarray)->np.ndarray:
    key_inv = Matrix(founded_key).inv_mod(26)
    key_inv = np.array(key_inv).astype(int)
    decrypted = dot(key_inv, sniffed_cyphertext) % 26
    return np.transpose(decrypted)



def main():
    sniffed_cyphertext = "VHECVJZHSPMVLUTAIYROHDTWEUWIGOLAMZLLLECIZSSZJYKJKTIXFIGVKWFS"
    block_size = 5
    sniffed_plaintext = "ILCIFRARIODIHILLAPPARTIEN"

    sniffed_plaintext = format_text(sniffed_plaintext,block_size)
    sniffed_cyphertext = format_text(sniffed_cyphertext,block_size,True)
    known_cyphertext = sniffed_cyphertext[:block_size,:block_size]

    logging.info("Sniffed plaintext: \n{sniffed_plaintext}".format(sniffed_plaintext = sniffed_plaintext))
    logging.info("Known_cyphertext: \n{known_cyphertext}".format(known_cyphertext = known_cyphertext))

    founded_key = attack(known_cyphertext, sniffed_plaintext, block_size)
    decrypted = decrypt(founded_key,sniffed_cyphertext)

    logging.info("Decrypted: \n{decrypted}".format(decrypted = decrypted))
    print("Decrypted: \n{text}".format(text = number_to_string(decrypted)))

if __name__ == "__main__":
    main()