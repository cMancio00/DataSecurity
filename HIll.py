import numpy as np
from numpy.linalg import inv


def sring_to_number(message:str)-> np.ndarray:
    message = message.upper()
    return np.asanyarray(list(message.encode('ascii'))) - 65


def crypt(plaintext:str, key:np.ndarray, block_size:int=2):
    plaintext = sring_to_number(plaintext)
    for i in range(0, len(plaintext), block_size):
        yield (key @ plaintext[i:i+block_size]) % 26


def decrypt(ciphertext:np.ndarray, key:np.ndarray):
    key = inv(key) % 26
    for block in ciphertext:
        block_to_yield = np.squeeze(np.asarray(block))
        yield (key @ block_to_yield) % 26

def get_text(plaintext:np.array)->str:
    text = list()
    for block in plaintext:
        block = np.squeeze(np.asarray(block))
        for number in block:
            letter = round(number,0) % 26
            text.append(chr(int(letter)+65))
    return "".join(text)
    

def main():
    key = np.matrix([[7,8],[19,3]])
    key2 = np.matrix([[2,3],[5,7]])
    key3 = np.matrix([[2,0],[0,1]])
    message = "Friday"
    print("Message to crypt: {message}".format(message = message))
    print("Crypting message {message}".format(message = sring_to_number(message)))
    ciphertext = crypt("Friday",key=key3)
    plaintext = decrypt(ciphertext, key=key3)
    print("Decrypted message {message}".format(message = get_text(plaintext)))


if __name__ == "__main__":
    main()
