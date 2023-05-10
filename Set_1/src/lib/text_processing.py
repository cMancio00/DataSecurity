from collections import Counter
from lib.string_preprocessing import add_padding

def read_text_file(text_file: str) -> str:
        text = open(text_file, "r")
        while True:
            line = text.readline()
            if not line:
                break
            yield line

def remove_special_characters(line: str) -> str:
    characters_to_remove = [" ",",",".",";","`","'","!","?","(",")","[","]","{","}","<",">","/",":","\n", \
                            "\"","|","@","#","$","%","^","&","*","-","+","=","_","~","0","1","2","3","4","5","6","7","8","9"]
    for character in characters_to_remove:
        line = line.replace(character, "")
    return line.upper()

def sort_by_name(dictionary: dict[str, float]) -> dict[str, float]:
    return {key: value for key, value in sorted(dictionary.items(), key=lambda item: item[0])}

def calculate_frequency(dictionary: dict[str, int]) -> dict[str, float]:
    total = sum(dictionary.values())
    return {key: value/total for key, value in dictionary.items()}

def m_gram_split(line: str, m_gram_len: int) -> list[str]:
    line = add_padding(line, m_gram_len,"x")
    char = list()
    for i in range(0,len(line),m_gram_len):
        m_gram = line[i:i+m_gram_len]
        if "x" not in line[i:i+m_gram_len]:
            char.append(m_gram)
    return char

def process_text_file(text: str,m_gram_len:int) -> dict[str, int]:
    text_gen = read_text_file(text)
    count = Counter()
    for line in text_gen:
        line = remove_special_characters(line)
        line = m_gram_split(line, m_gram_len)
        count.update(line)
    count = dict(count)
    frequency = calculate_frequency(count)
    return sort_by_name(frequency)