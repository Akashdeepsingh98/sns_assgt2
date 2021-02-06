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


def main():
    
    pass


if __name__ == '__main__':
    main()
