from scanner import process_data
from table.tokens import tokens_table
from table.parsing import parsing_table
from table.key_lfg import key_converter_lfg
from table.key_tokens import key_tokens_converter
from table.key_terminals import key_terminals
from scanner import token_ids_table

tokens = tokens_table()
data = process_data(4)
table = parsing_table()
tokens_table_var = tokens_table()
token_table_verify = tokens_table()
topStack = []
tokens_ids = token_ids_table

if __name__ == "__main__":
    if ( "main" not in tokens_ids ):
        raise Exception("Program did not finished in the form void main (void) { return }")
    index_main = tokens_ids.index('main')
    
    symbol = "$"
    inputBuffer = ['$'] + data

    topStack.append('$')
    topStack.append('S')

    # non-terminals 
    with open('./util/lfg.txt', 'r') as file:
        content = file.read()
    # productions 
    with open('./util/productions.txt', 'r') as file:
        productions = file.readlines()

    action = '' # next action to do 
    line = '' # used to convert string to array 

    # set intials vars 
    get_row = key_converter_lfg(topStack[-1]) # used to get the row number 
    token = inputBuffer[-1] # last element in the input buffer 
    get_column = key_tokens_converter(token) # used to get the value of the column  
    column = key_terminals(get_column) # used to get the column number 

    while ( topStack[-1] != '$' ): # while stack is not empty.
        # print('-----------------------------------------')
        # print(topStack)
        # print(inputBuffer)
        # print('-----------------------------------------')

        if topStack == ['$', 'H', ')', 'void', '(', 'ID', 'void', 'A']:

            value = inputBuffer[-2]
            val = inputBuffer[-1]
            if (value[1] != (index_main+1) and value[0] == 33 and val == 9) :
                topStack.pop()
                topStack.append('A')
                topStack.append('B')
            else:
                pass
        # in case the input is a token symbol 
        if isinstance(inputBuffer[-1], tuple):
            tokenTemp = inputBuffer[-1]
            get_int = tokenTemp[0]

            terminal = key_tokens_converter(get_int)
            if (str(terminal) == "integer_cons"):
                terminal = "INTEGER"
            elif (str(terminal) == "integer_float"):
                terminal = "FLOAT"
            elif (str(terminal) == "strings"):
                terminal = "STRING"
            token = key_terminals(terminal)
        else:
            get_int = inputBuffer[-1]
            if (get_int == '$'):
                raise Exception("Program did not finished in the form void main (void) { return }")
            terminal = key_tokens_converter(get_int) 
            token = key_terminals(terminal)  # column number for terminal symbols 


        if (key_terminals(topStack[-1]) != -1):
            topStack.pop()
            inputBuffer.pop()
            continue

        else:
            convert_nt_to_num = key_converter_lfg(topStack[-1])

            if ( convert_nt_to_num == 100):
                topStack.pop()
                continue

            action = table[int(convert_nt_to_num)][int(token)]
            
            line = productions[int(action) - 1].strip()

            if (key_terminals(line) != -1):
                topStack.pop()
                inputBuffer.pop()
                continue
            

            topStack.pop() # take out the non terminal from top of stack
            action_production = line.split()
            action_production.reverse()
            for i in action_production: # append the production 
                topStack.append(i)


    if (len(inputBuffer) == 0 and len(topStack) > 0):
        print("Program did not finished in the form void main (void) { return } ")
    if (topStack[-1] == '$' ):
        print("PASSED")
