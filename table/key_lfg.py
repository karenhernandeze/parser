def key_converter_lfg(value: str):
    keys = {"S": 1,
            "A": 2,
            "B": 3,
            "B'": 4,
            "C": 5,
            "C'": 6,
            "D": 7,
            "E": 8,
            "F": 9,
            "G": 10,
            "H": 11,
            "I": 12,
            "J": 13,
            "K": 14,
            "K'": 15,
            "L": 16,
            "M": 17,
            "N": 18,
            "O": 19,
            "P": 20,
            "P'": 21,
            "Q": 22,
            "R": 23,
            "R'": 24,
            "Z": 25,
            "T": 26,
            "T'": 27,
            "U": 28,
            "V": 29,
            "V'": 30,
            "W": 31,
            "X": 32,
            "Y": 33,
            "ε": 100
            }
    return keys[value]