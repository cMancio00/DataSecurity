import numpy as np
from sympy import Matrix
import logging
from os import mkdir
from os.path import exists
from lib.string_preprocessing import prepare_message, number_to_string

if not exists("Logs"):
    mkdir("Logs")
logging.basicConfig(format='%(asctime)s - %(message)s\n', filename='Logs/hill_cipher.log', filemode='w', level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S')

def crypt(plaintext:np.ndarray, key:np.ndarray,block_size)->np.ndarray:
    plaintext.resize((int(len(plaintext)/block_size) , block_size))
    ciphertext = np.dot(plaintext, key) % 26
    logging.info("[CIPHERTEXT]\n{ciphertext}\n{text}".format(ciphertext = ciphertext, text = number_to_string(ciphertext)))
    return ciphertext

def decrypt(ciphertext:np.ndarray, key:np.ndarray)->np.ndarray:
    key_inv = Matrix(key).inv_mod(26)
    key_inv = np.array(key_inv).astype(float)
    logging.info("[KEY INVERSE]\n{key_inv}".format(key_inv = key_inv))
    plaintext = np.dot(ciphertext,key_inv) % 26
    logging.info("[PLAINTEXT]\n{plaintext}\n{text}".format(plaintext = plaintext, text = number_to_string(plaintext)))
    return plaintext

def generate_key(block_size:int)->np.ndarray:
    while True:
        key = np.random.randint(0, 26, size=(block_size, block_size))
        try:
            Matrix(key).inv_mod(26)
        except ValueError:
            continue
        logging.info("[KEY GENERATED]\n{key}".format(key=key))
        return key

def main():
    message = "Il cifrario di Hill appartiene ai cifrari monoalfabetici a blocchi"
    block_size = np.random.randint(2, 10)
    key = generate_key(block_size)
    message = prepare_message(message, block_size)
    crypted = crypt(message, key, block_size)
    decrypted = decrypt(crypted, key)
    print("Message was: {message}".format(message = number_to_string(decrypted)))


if __name__ == "__main__":
    main()
