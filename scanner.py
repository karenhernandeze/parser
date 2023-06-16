from table.transitions import transitions_table
from table.key import key_converter
from table.tokens import tokens_table
import os.path

# White spaces = blanks, newlines, and tabs
delim_tokens = [" ", "\n", "\t", ""]
keywords= ["int", "float", "if", "else", "read", "write", "string", "for", "while", "return", "void"]
special_symbols = ["+", "-", "*", ";", ",", "(", ")", 
                   "[", "]", "{", "}", "<", ">", "=", "!", "/", ".", '"', ]

# retrieve the transition table, given in a list format 
transition_states = transitions_table()
# retrieve the tokens table, given in an dictionary data type 
tokens = tokens_table()
# outputs table. Symbol Table, for all valid Tokens. 1) Integer 2) Floats 3) Tokens 4) Strings 
integer_table = []
float_table = []
token_ids_table = []
strings_output_table = []

# temp arrays to store the 'words' and numbers, before being added to the outputs table 
string_table = []
number_table = []

output = []

error_states = [38,39,40,41]
symbols_states = [26,27,28,29,30,31,32]

# function used to know what type of char are we getting 
def get_value(char: str) -> str:
    if char.isdigit():
        return "digit"
    elif char.isalpha():
        return "letter"
    elif char in special_symbols:
        return char 
    elif char in delim_tokens: 
        return "delim" 
    else:
        return "rare_char"

# funciton used to construct the output array. 
def add_to_output(token: str, type: str):
    # for all the tokens, we first get the value from the token id table. e.g. if we get an int
    # the value return will be 1, given it is the index for that symbol. Next if it is and ID, string 
    # or number, we will get the index of that symbol table, before hand they have been already added 
    # to it respective table. Finally the value is added to the output array 
    if type == "ID": 
        del string_table[:]
        value = tokens["ID"]
        index = token_ids_table.index(token)
        output.append((value, index+1))
    elif type == "KW":
        value = tokens[token]
        output.append(value)
        del string_table[:]
    elif type == "string":
        value = tokens["strings"]
        index = strings_output_table.index(token)
        output.append((value, index+1))
        del string_table[:]
    elif type == "num1":
        value = tokens["integer_cons"]
        index = integer_table.index(token)
        output.append((value, index+1))
        del number_table[:]
    elif type == "num2":
        value = tokens["integer_float"]
        index = float_table.index(token)
        output.append((value, index+1))
        del number_table[:]
    else:
        value = tokens[token]
        output.append(value)

def process_data(test_num):
    open_file = f"tests/test{test_num}.txt"
    with open(open_file, 'r', encoding='utf-8') as file:
        state = 1
        # flag used to check if strings and comments have been closed 
        flag = 0
        # identifier used to get the line where the code threw an exception 
        i = 1

        while True:
            # print the ouput also in the next .txt file to assert true or false the tests 
            if os.path.exists(f"tests/output_results/results{test_num}.txt"):
                os.remove(f"tests/output_results/results{test_num}.txt")
            f = open(f"tests/output_results/results{test_num}.txt", "a")

            # get char to read
            char = file.read(1).lower()
            if not char: 
                # if it reached the end of the file and the comment or string hasnt been closed an exception is thrown 
                if state == 7 or state == 8:
                    f.write(f"Comments not Closed. \nError in line: {i}")
                    raise Exception(f"Comments not Closed. \nError in line: {i}")
                elif state == 12:
                    f.write(f"String not Closed. \nError in line: {i}")
                    raise Exception(f"String not Closed. \nError in line: {i}")
                print('Reached end of file')
                break
                    
            # check if the char to be defined is letter, digit, delim, sp sym or rare
            transition = get_value(char) 
            # convert the char to int to be able to use the key from the transitions table
            get_int = key_converter(transition)
            # get the new state given the transition

            # if the state is bigger than 13 it means and invalid char has been given. 
            if state > 13:
                f.write(f"Invalid Character. \nError in line: {i}")
                raise Exception(f"Invalid Character. \nError in line: {i}")
            else:
                # get the new state given the transition 
                # e. g. transition_state[1][/] -> transition_state[1][17] = 6 
                # new state = 6
                new_state = transition_states[state][get_int]
                state = int(new_state)

                # delim_tokens 
                if state == 1:
                    if char == '\n':
                        i += 1
                    # ignore the delimeters
                    pass
                # read all the chars from the string 
                # if it is letter
                elif state == 9:
                    # append it to the temp array of strings 
                    string_table.append(char)
                # integers or floats, save to table 
                elif state == 10 or state == 11 or state == 13:
                    # append it to the temp array of numbers 
                    number_table.append(char) 
                # if a string is beginning
                elif state == 12: 
                    # append it to the temp array of strings 
                    string_table.append(char)
                    # flag used to check if the string is closed. Set to 1.  
                    flag = 1
                # means a string came up and has been closed 
                elif state == 14:
                    # set flag to 0, meaning no error. 
                    flag = 0
                    str1 = ""
                    for e in string_table:
                        str1 += e 
                    str1 = str1 + '"'
                    # add the string to the output string table, given it reached the terminal state 
                    strings_output_table.append(str1)
                    add_to_output(str1, "string")
                    # once reached a termimal state, set state to 1 
                    state = 1
                    continue
                # if char is a special symbol 
                elif state >= 15 and state <= 25:
                    add_to_output(char, "")
                    # once reached a termimal state, set state to 1 
                    state = 1
                    continue
                # a division was made
                elif state == 33:
                    add_to_output('/', "")
                    state = 1
                    continue
                # a comment was opened and now closed, too. set flag to 0 
                elif state == 34:
                    # set flag to 0, meaning no error. 
                    flag = 0
                    state = 1
                    continue
                # ids or keywords 
                elif state == 35:
                    # it reached the final state of an id, check if it is keyword or ids
                    str1 = ""
                    for e in string_table:
                        str1 += e 
                    if str1 in keywords:
                        add_to_output(str1, "KW")
                    else: 
                        if str1 in token_ids_table:
                            pass 
                        else:
                            token_ids_table.append(str1)
                        # if it is an id append it to the ids table 
                        add_to_output(str1, "ID")
                    # if the string table is empty it means a special symbols has come up after inmeditaly after an id 
                    if not string_table:
                        # if something came up inmediatly after but it was a delimiter, do not add 
                        if char not in delim_tokens:
                            add_to_output(char, "")
                    state = 1
                    continue
                # integers
                elif state == 36:
                    str1 = ""
                    for e in number_table:
                        str1 += e 
                    if str1 in integer_table:
                        pass 
                    else:
                        integer_table.append(str1)
                    add_to_output(str1, "num1")
                    state = 1
                    # to add delimeters that are next to a num e.g. 4>5
                    if char not in delim_tokens:
                        add_to_output(char, "")
                    continue
                # floats
                elif state == 37:
                    str1 = ""
                    for e in number_table:
                        str1 += e 
                    if str1 in float_table:
                        pass 
                    else:
                        float_table.append(str1)
                    add_to_output(str1, "num2")
                    state = 1
                    # too add delimeters that are next to a num e.g. 4.5>5
                    if char not in delim_tokens:
                        add_to_output(char, "")
                    continue
                # case for special symbols '<' '>' '!' '='
                elif state in symbols_states:
                    if state == 26:
                        add_to_output('<=', "")
                    elif state == 27:
                        add_to_output('<', "")
                    elif state == 28:
                        add_to_output('>=', "")
                    elif state == 29:
                        add_to_output('>', "")
                    elif state == 30:
                        add_to_output('==', "")
                    elif state == 31:
                        add_to_output('=', "")
                    elif state == 32:
                        add_to_output('!=', "")
                    state = 1
                # case for the comments, check they are correctly closed flag = 1
                elif state == 7 or state == 8:
                    flag = 1
                # if something went to an error state 
                elif state in error_states:
                    if state == 38:
                        f.write(f"Invalid Character. \nError in line: {i}")
                        raise Exception(f"Invalid Character. \nError in line: {i}")
                    elif state == 39:
                        f.write(f"Invalid ID. \nError in line: {i}")
                        raise Exception(f"Invalid ID. \nError in line: {i}")
                    elif state == 40: 
                        f.write(f"Invalid Number. \nError in line: {i}")
                        raise Exception(f"Invalid Number. \nError in line: {i}")
                    elif state == 41:
                        f.write(f"Invalid String. \nError in line: {i}")
                        raise Exception(f"Invalid String. \nError in line: {i}")
                    raise Exception(f"Error in line {i}")        

        print("Scanner Output: ")
        print(output)
        # for i in output:
        #     f.write(str(i)+'\n')
        #     print((i))
        
        j = 1
        print(f"Integer Constants Table:")
        if not integer_table:
            print("Table Empty.")
        for i in integer_table:
            f.write(f"Entry {j}: "+ str(i)+'\n')
            print(f"Entry {j}: ", i)
            j += 1

        k = 1
        print(f"Floats Constants Table:")
        if not float_table:
            print("Table Empty.")
        for fn in float_table:
            f.write(f"Entry {k}: "+ str(fn)+'\n')
            print(f"Entry {k}: ", fn)
            k += 1

        l = 1
        print(f"Token IDs Table:")
        if not token_ids_table:
            print("Table Empty.")
        for t in token_ids_table:
            f.write(f"Entry {l}: "+ t+'\n')
            print(f"Entry {l}: ", t)
            l += 1
        
        m = 1
        print("Strings Table:")
        if not strings_output_table:
            print("Table Empty.")
        for s in strings_output_table:
            f.write(f"Entry {m}: "+ s+'\n')
            print(f"Entry {m}: ", s)
            m += 1

    f.close()

    reversed_array = output[::-1]
    return reversed_array

def id_table ():
    return token_ids_table

# if __name__ == "__main__":
#     # change the test_num variable depending on which test you want to run 
#     test_num = 4
#     process_data(test_num)
    