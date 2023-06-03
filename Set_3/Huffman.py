
def find_min_probability(probabilities: list[tuple]) -> tuple:
    return min(probabilities, key=lambda x: x[1])

def generate_code(codes:str) -> dict:
    codes = codes.split(',')
    for i in range(len(codes)):
        codes[i] = codes[i].replace('(','').replace(')','')
    code = {}
    if len(codes) == 1:
        code[codes[0]] = '0'
    else:
        for index,element in enumerate(codes):
            code[element] = '1'*index + '0'
        last = code.popitem()
        code[last[0]] = last[1][:-1]
    return code        


def huffman_encoding(alphabet: list, probabilities: list) -> dict:
    codes = dict(zip(alphabet,probabilities))
    while len(codes) > 1:
        min_prob = find_min_probability(codes.items())
        removed = (min_prob[0],codes.pop(min_prob[0]))
        min_prob = find_min_probability(codes.items())
        if min_prob[1] > removed[1]:
            codes['(' + min_prob[0] + ',' + removed[0] + ')'] = min_prob[1] + removed[1]
        else:
            codes['(' + removed[0] + ',' + min_prob[0] + ')'] = removed[1] + min_prob[1]
        codes.pop(min_prob[0])
    print(codes)
    return generate_code(list(codes.keys())[0])

def prefix_free_decoding(code: dict, encoded: str) -> str:
    code = {codes:letter for letter,codes in code.items()}
    decoded = ''
    while encoded:
        for key in code.keys():
            if encoded.startswith(key):
                decoded += code[key]
                encoded = encoded[len(key):]
    return decoded


def main():
    print(huffman_encoding(['a','b','c','d'],[0.5,0.25,0.125,0.125]))
    code = huffman_encoding(['a','b','c','d'],[0.9,0.05,0.025,0.025])
    decoded = prefix_free_decoding(code,'1101111010000111') # "cdbbaaad"
    print(decoded)
    assert decoded == 'cdbbaaad'


if __name__ == '__main__':
    main()