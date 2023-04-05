
from numpy import unique, gcd
import numpy as np
from lib.string_preprocessing import add_padding, sring_to_number, number_to_string

chypertext = \
"OKZARVGLNSLFOQRVVBPHHZAMOMEVHLBAITLZOWSXCSZFEQFICOOVDXCIISOOVXEIYWNHHLVQHSOWD"+\
"BRPTTZZOWJIYPJSAWQYNOYRDKBQKZPHHTLIHDEMICGYMSEVHKVXTQPBWMEWAZZKHLJMOVEVHJYSJR"+\
"ZTUMCVDGLZVBUIWOCPDZVEIGSOGZRGGOTAHLCSRSCXXAGPDYPSYMECRVPFHMYWZCYHKMCPVBPHYIF"+\
"WDZTGVIZEMONVYQYMCOOKDVQIMSOKLBUEBFZISWSTVFEWVIAWACCGHDRVVZOOBANRYHSSQBUIMSDW"+\
"VBNRXSSOGLVWKSCGHLNRYHSSQLVIYCFHVWJMOVEKRKBQMOOSVQAHDGLGWMEOMCYOXMEEIRTZBCFLZ"+\
"BVCVPRQVBLUHLGSBSEOUWHRYHSSEIEVDSCGHZRGOSOPBBUIQWNHRZFEIRPBWMEXCSPASBLXZFCWWW"+\
"EMZGLDDBUIOWNTHVPICOOTRZOMYRPBKMEIIHCOQKRWCSNFRAFIYWEKLBUSPHEVHAYMBVESVBGVZAZ"+\
"FVPRAJIWRQMIIMUZPDKXXJHSSRBUIMGTRHBUIMSHCXTQFZBZFHBHVIOYRWPRXCFPSRNGLZAVBHEVX"+\
"OVPMZMEIAIWZBIJEMSEVDBGLZMHSUMGVVWWWQOGLZCCPLARWYSNZLVRXCOEHKMLAZFPGLVXMIUHWW"+\
"PVXDBECWPRJDBLZQQTLOALFHBUIKOEVZWHPYPPRLNSMXIWHWPNXOCZHKMLOISH"

def split_text(text: str, m_gram_len: int) -> list[str]:
    m_grams = list()
    for i in range(0,len(text),m_gram_len):
        m_gram = text[i:i+m_gram_len]
        m_grams.append(m_gram)
    return m_grams

def get_high_frequency_m_grams(m_grams: list[str]) -> dict[str, int]:
    high_freq = dict()
    for m_gram in unique(m_grams):
        count = m_grams.count(m_gram)
        if count > 2:
            high_freq[m_gram] = count
    return high_freq

def get_positions(m_grams: list[str], element: str) -> list[int]:
    positions = list()
    for m_gram in range(len(m_grams)):
        if m_grams[m_gram] == element:
            positions.append(m_gram)
    print("Element {element} positions:\n{positions}".format(positions=positions,element=element))
    return positions

def get_distances(positions: list[int], element:str) -> list[int]:
    distances = list()
    for position in positions[1:]:
        distances.append(position - positions[0])
    print("Elemt {element} distances:\n{distances}".format(distances=distances,element=element))
    return distances

def build_matrix(text: str, m: int) -> np.ndarray:
    text = add_padding(text, m)
    matrix = np.array([sring_to_number(text[i:i+m]) for i in range(0,len(text),m)])
    return np.transpose(matrix)

def coincidence_index(array: np.ndarray) -> float:
    n = len(array)
    sum = 0
    for i in range(26):
        frequency = np.count_nonzero(array == i)
        sum += (frequency*(frequency-1))/(n*(n-1))
    return sum

def frequency_vector(array: np.ndarray) -> np.ndarray:
    frequency_vector = np.zeros(26)
    for i in range(26):
        frequency_vector[i] = np.count_nonzero(array == i)
    return frequency_vector


def main():
    m_gram_len = 3
    m_grams = split_text(chypertext, m_gram_len)
    high_frequency = get_high_frequency_m_grams(m_grams)
    print("High frequency m_grams:\n{high_frequency}".format(high_frequency=high_frequency))

    key_lenghts = list()
    for key in high_frequency.keys():
        positions = get_positions(m_grams, key)
        distances = get_distances(positions, key)
        key_lenght = gcd.reduce(distances)
        key_lenghts.append(key_lenght)
    print("Possible key lenghts:\n{key_lenghts}".format(key_lenghts=key_lenghts))  

    m = key_lenghts[0]
    cyphertext = build_matrix(chypertext, m)
 

    indexes = list()
    for row in cyphertext:
        indexes.append(coincidence_index(row))

    for index in range(len(indexes)):
        print("Row {row_number}: {coincidence}".format(row_number=index,coincidence=indexes[index]))

    p = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
    
    key = list()
    for row in cyphertext:
        max_list = list()
        for g in range(26):
            sum = 0
            for j in range(26):
                sum += p[j]*(frequency_vector(row)[(g+j)%26]/(len(row)/m))
            max_list.append(sum)
        key.append(max_list.index(max(max_list)))
    print(key)
    print(number_to_string(key))

    ciphertext = np.transpose(cyphertext)
    ciphertext = ciphertext.ravel()
    decripted = list()
    for i in range(len(ciphertext)):
        decripted.append((ciphertext[i]-key[i%m])%26)
    print(number_to_string(decripted))

    

if __name__ == "__main__":
    main()