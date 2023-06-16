# function used to get the value, given a key. In this case it is the same order as the 
# first row from the transitions table. Given it is the value used to find the new state,
# given an incoming char.  
def key_converter(value: str):
    keys = {"letter": 0,
            "digit": 1,
            "+": 2,
            "-": 3,
            "*": 4,
            ";": 5,
            ",": 6,
            "(": 7,
            ")": 8,
            "[": 9,
            "]": 10,
            "{": 11,
            "}": 12,
            "<": 13,
            ">": 14,
            "=": 15,
            "!": 16,
            "/": 17,
            ".": 18,
            '"': 19,
            "delim": 20,
            "rare_char": 21,
            }
    return keys[value]