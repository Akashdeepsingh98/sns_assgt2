import numpy as np
import socket

CIPHER_MATRIX = np.array([
    [-3, -3, -4],
    [0, 1, 1],
    [4, 3, 4]
])

CIPHER_MATRIX_INV = np.array([
    [1, 0, 1],
    [4, 4, 3],
    [-4, -3, -3]
])

ENCODING_RULE = {' ': 27}
for i in range(0, 26):
    ENCODING_RULE[chr(i+ord('A'))] = i+1

KEY = '1101'.lstrip('0')


def getp(data):
    while len(data) % 3 != 0:
        data += ' '
    p = np.array([ENCODING_RULE[data[i]] for i in range(len(data))])
    p = np.reshape(p, (3, len(data)//3), 'F')
    return p


def getRemainder(data: str) -> str:
    len_data = len(data) - len(KEY) + 1
    data_list = list(data)

    for curpos in range(len_data):
        if data_list[curpos] == '1':
            for i in range(len(KEY)):
                data_list[curpos+i] = '1' if KEY[i] != data_list[curpos+i] else '0'

    return ''.join(data_list)[len_data:]


def getCRC(data: str) -> str:
    binString = (''.join(format(ord(x), 'b') for x in data))
    newString = binString + '0' * (len(KEY)-1)
    remainder = getRemainder(newString)
    code = binString+remainder
    return code


def main():
    data = 'EVN'
    p = getp(data)
    EncData = np.dot(CIPHER_MATRIX, p)
    print(EncData)
    E = getCRC(data)
    print(E)


if __name__ == '__main__':
    main()
