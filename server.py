import numpy as np
import socket
import pickle

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

DECODING_RULE = {}
for key in ENCODING_RULE.keys():
    DECODING_RULE[ENCODING_RULE[key]] = key

KEY = '1101'.lstrip('0')


def decryptp(dataMarix):
    p = np.dot(CIPHER_MATRIX_INV, dataMarix)
    p = np.reshape(p, (p.shape[0] * p.shape[1]), 'F')
    text = ''
    for i in range(p.shape[0]):
        text += DECODING_RULE[p[i]]
    return text.rstrip()


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
    #code = binString+remainder
    return remainder


def main():

    s = socket.socket()
    port = 5001
    s.bind(('', port))
    s.listen(2)

    c, addr = s.accept()
    data = c.recv(1024000)
    data1 = data[:data[1:].find(b'\x80')]
    data1 += b'.'

    data2 = data[data[1:].find(b'\x80'):]
    data2 = data2[1:]

    EncData = pickle.loads(data1)
    E = pickle.loads(data2)

    recText = decryptp(EncData)
    print('The received text is: ', end='')
    print(recText)
    
    if getCRC(recText) == E:
        print('String is Correct')
    else:
        print('String is Incorrect')
    c.close()
    s.close()


if __name__ == '__main__':
    main()
