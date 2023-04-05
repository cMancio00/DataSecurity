
from numpy import unique, gcd

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

if __name__ == "__main__":
    main()