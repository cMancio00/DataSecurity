import numpy as np
import logging

def add_padding(message:str, block_size:int,padding_value:str = "X" )->str:
    if len(message) % block_size != 0:
        message += padding_value * (block_size - (len(message) % block_size))
    return message

def sring_to_number(message:str)-> np.ndarray:
    message = message.upper()
    return np.asanyarray(list(message.encode('ascii'))) - 65

def number_to_string(message:np.ndarray)->str:
    message = np.ravel(message)
    message = list(message)
    return "".join([chr(int(letter)+65) for letter in message])

def remove_spaces(message:str)->str:
    return message.replace(" ", "")

def prepare_message(message:str, block_size:int)->str:
    message = message.upper()
    logging.info("[MESSAGE TO CRYPT]\n{message}".format(message = message))
    message = remove_spaces(message)
    message = add_padding(message, block_size)
    logging.info("[MESSAGE PROCESSED]\n{message}".format(message = message))
    message = sring_to_number(message)
    logging.info("[MESSAGE TO NUMBERS]\n{message}".format(message = message))
    return message