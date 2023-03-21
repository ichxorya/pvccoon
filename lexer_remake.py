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
    source_code = utils.source_code

    # Get the maps.
    map_state = utils.map_state
    map_key = utils.map_key

    # Initialize the starting state and related variables.
    current_state = "0"
    current_token = ""
    tokens = []

    next_position = 0

    # Loop through the source code.
    while next_position < len(source_code):
        # Get the next character.
        next_char = source_code[next_position]

        # Get the next state.
        next_state = utils.get_next_state(current_state, next_char)

        # If current character is a whitespace/new line, skip it.
        if next_char in utils.new_line:
            next_position += 1
            if current_state != "86":
                tokens.append([current_token, current_state])
                current_state = "0"
                current_token = ""
                continue
            else:
                next_position += 1
        
        match next_state:
            case "69420":
                sys.exit(1)
            case "":
                next_position += 1
                tokens.append([current_token, current_state])
                current_state = utils.get_next_state("0", next_char) 
                current_token = "" + next_char
                continue
            case None:
                tokens.append([current_token, current_state])
                current_state = "0"
                current_token = ""
                next_position += 1
            case _: 
                if current_state not in ["86", "83"] and next_char in utils.whitespaces:
                    next_position += 1
                    tokens.append([current_token, current_state])
                    current_state = "0"
                    current_token = ""
                    continue    
                current_token = current_token + next_char
                current_state = next_state
                next_position += 1
                continue

    tokens = list(filter(lambda a: a[0] != " ", tokens))
    tokens = list(filter(lambda a: a[0] != "", tokens))
    tokens = list(filter(lambda a: a[0] != "\t", tokens))
    print(tokens)
    # Write the tokens to a file.
    utils.write_tokens(tokens)       
