# Import libraries.
from utils import Utils
import sys

# Main function.
if __name__ == "__main__":
    # Check the arguments.
    if len(sys.argv) < 2:
        print("Usage: python lexer.py <path>")
        sys.exit(1)

    path = sys.argv[1]

    # Initialize the utils.
    utils = Utils(path)

    # Get the source code.
    source_code = utils.source_code + " "

    # Get the maps.
    map_state = utils.map_state
    map_key = utils.map_key

    # Initialize the starting state and related variables.
    current_state = "0"
    current_token = ""
    tokens = []

    # Initialize the starting value for position in file
    start_position = [1, 1]
    char_line = 1
    char_column = 0

    # Initialize the temp parameters
    next_position = 0
    next_char  = "" 
    

    # Loop through the source code.
    while next_position < len(source_code):

        # Check if arriving at new line or not 
        if next_char in utils.new_line:
            char_line += 1
            char_column = 0

        # Get the next character.
        next_char = source_code[next_position]

        # Get the next state.
        def find_next_state(state, next):
            if next in utils.whitespaces:
                return utils.get_next_state(state, "whitespaces")
            elif next in utils.new_line:
                return utils.get_next_state(state, "newline")
            else:
                return utils.get_next_state(state, next)
        next_state = find_next_state(current_state, next_char)
        
        # Check the next state
        match next_state:
            case "69420":       # Error
                print(utils.get_error_line(char_line, char_column))
                sys.exit(1)
            case "" | None:            # Any case that lead to "" (mean there's no next stage with next character) or None (mean that the current state is end state)
                if source_code[next_position - 1]  not in utils.whitespaces and source_code[next_position - 1] not in utils.new_line:   # Not adding token to tokens if token is created from whitespaces or newline
                    tokens.append([current_token, current_state, start_position, [char_line, char_column]])
                current_state = utils.get_next_state("0", next_char)                      
                if next_char == "\"":       # Not adding " to string
                    current_token = "" 
                else:
                    current_token = "" + next_char 
                next_position += 1
                char_column += 1
                start_position = [char_line, char_column]
                continue     
            case "88":          # Token is note (/**/). Not adding to tokens  
                current_state = "0"                     
                current_token = ""
                next_position += 1
                char_column += 1
                start_position = [char_line, char_column]
                continue
            case "105":         # Token is note (//). Not adding to tokens
                current_state = "0"                     
                current_token = ""
                next_position += 1
                char_column += 1
                start_position = [char_line + 1, 1]
                continue
            case "100":         # When next char is \, add if no other state than 83
                current_state = next_state
                next_position += 1
                if find_next_state(current_state, source_code[next_position]) == "83":
                    current_token = current_token + next_char
                char_column += 1 
                continue
            case "102":         # Add tab to string
                current_token = current_token + '\t'
                current_state = "83"
                next_position += 1
                char_column += 1 
                continue
            case "101":         # Add newline to string
                current_token = current_token + '\n'
                current_state = "83"
                next_position += 1
                char_column += 1 
                continue
            case "103":         # Add " to string
                current_token = current_token + '\"'
                current_state = "83"
                next_position += 1
                char_column += 1 
                continue
            case "104":         # Add \ to string
                current_token = current_token + '\\'
                current_state = "83"
                next_position += 1
                char_column += 1 
                continue
            case _:             # All states that can be follower by another state
                if next_char != "\"":           # Remove " from string
                    current_token = current_token + next_char
                current_state = next_state
                next_position += 1
                char_column += 1 
                continue
    
     # add end token
    tokens.append(["$", "999", [char_line, char_column],[char_line, char_column]])

    # Remove token create bt string of whitespace and newline
    tokens = list(filter(lambda a: a[0] != "", tokens))  

    # Write the tokens to a file.
    utils.write_tokens(tokens)   
    utils.write_verbose(tokens)   
