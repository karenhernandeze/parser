def key_tokens_converter(value: str):
    keys = {1: "int",
            2: "if",
            3: "read",
            4: "float",
            5: "else",
            6: "write",
            7: "string",
            8: "while",
            9: "void",
            10: "for",
            11: "return",
            12: "+",
            13: "-",
            14: "*",
            15: "/",
            16: "<",
            17: "<=",
            18: ">",
            19: ">=",
            20: "==",
            21: "!=",
            22: "=",
            23: ";",
            24: ",",
            25: '"',
            26: ".",
            27: "(",
            28: ")",
            29: "[",
            30: "]",
            31: "{",
            32: "}",
            33: "ID",
            34: "integer_cons",
            35: "integer_float",
            36: "strings"
            }
    return keys[value]