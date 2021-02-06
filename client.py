import numpy as np

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


def getp(data):
    while len(data)%3!=0:
        data+=' '
    p = np.array([ENCODING_RULE[data[i]] for i in range(len(data))])
    p = np.reshape(p,(3,len(data)//3),'F')
    return p

def getCRC(data):
    
    pass

def main():
    data = 'PENGUINS ARE ONE TO ONE'
    p = getp(data)
    encData = np.dot(CIPHER_MATRIX, p)
    print(encData)
    pass


if __name__ == '__main__':
    main()
