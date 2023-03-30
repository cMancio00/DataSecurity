import numpy as np
from numpy.linalg import inv
import logging

def sring_to_number(message:str)-> np.ndarray:
    message = message.upper()
    return np.asanyarray(list(message.encode('ascii'))) - 65

def add_padding(message:str, block_size:int)->str:
    if len(message) % block_size != 0:
        message += "X" * (block_size - (len(message) % block_size))
    return message

def check_key_is_valid(key:np.ndarray, block_size:int)->bool:
    if key.shape[0] != block_size or key.shape[1] != block_size:
        raise ValueError("Key must be a {block_size}x{block_size} matrix".format(block_size = block_size))
    if np.linalg.det(key) == 0:
        raise ValueError("Key must be invertible")

def crypt(plaintext:str, key:np.ndarray, block_size:int=2):
    plaintext = plaintext.replace(" ", "")
    plaintext = add_padding(plaintext, block_size)
    print("Message to crypt - {plaintext}".format(plaintext = plaintext.upper()))
    logging.basicConfig(format='%(asctime)s - %(message)s', filename='hill.log', filemode='w', level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S')
    plaintext = sring_to_number(plaintext)
    logging.info("[PLAINTEXT] - {plaintext}".format(plaintext = plaintext))
    for i in range(0, len(plaintext), block_size):
        logging.info("[CRYPTING BLOCK] - {block}".format(block = plaintext[i:i+block_size]))
        yield (key @ plaintext[i:i+block_size]) % 26


def decrypt(ciphertext:np.ndarray, key:np.ndarray):
    logging.basicConfig(format='%(asctime)s - %(message)s', filename='hill.log', filemode='w', level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S')
    key = inv(key) % 26
    for block in ciphertext:
        block_to_yield = np.squeeze(np.asarray(block))
        logging.info("[DECRYPTING BLOCK] - {block_to_yield}".format(block_to_yield = block_to_yield))
        yield (key @ block_to_yield) % 26

def get_text(numeric_text:np.array)->str:
    text = list()
    for block in numeric_text:
        block = np.squeeze(np.asarray(block))
        for number in block:
            letter = round(number,0) % 26
            text.append(chr(int(letter)+65))
    return "".join(text)
    

def main():

    message = "Easy peasi lemon squeezy"

    key = np.matrix([[2,3],[5,7]])

    block_size = key.shape[0]

    try:
        check_key_is_valid(key, block_size=block_size)
    except ValueError as e:
        print(e)
        return

    ciphertext = crypt(message,key=key, block_size=block_size)
    decrypted_message = decrypt(ciphertext, key=key)
    print("Decrypted message - {plaintext}".format(plaintext = get_text(decrypted_message)))



if __name__ == "__main__":
    main()
