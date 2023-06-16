# Tokens id table 
def tokens_table():
    token_dict = {}

    keys = ["int", #1
            "if", #2
            "read", #3 
            "float", #4
            "else", #5 
            "write", #6
            "string", #7 
            "while", #8
            "void", #9 
            "for", #10
            "return", #11
            "+", #12 
            "-", #13 
            "*", #14
            "/", # 15
            "<", #16
            "<=", #17
            ">", #18
            ">=", #19
            "==", #20
            "!=", #21
            "=", #22
            ";", #23
            ",", #24
            '"', #25
            ".", #26
            "(", #27
            ")", #28
            "[", #29
            "]", #30
            "{", #31
            "}", #32
            "ID", #33
            "integer_cons", #34
            "integer_float", #35
            "strings", #36
            ]

    for i, k in enumerate(keys):
        token_dict[k] = i + 1

    # for i in token_dict:
    #     print(i)
    return token_dict