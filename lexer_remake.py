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
        if next_char in utils.whitespaces:
            next_state = utils.get_next_state(current_state, "whitespaces")
        elif next_char in utils.new_line:
            next_state = utils.get_next_state(current_state, "newline")
        else:
            next_state = utils.get_next_state(current_state, next_char)
        
        # Check the next state
        match next_state:
            case "69420":       # Error
                sys.exit(1)
            case "":            # Any case that lead to "" (mean there's no next stage with next character) with cut the current token and save to tokens list, this case can deal with any next character that lead to end of current token (not counting whitespaces, may be add them later). e.g. i=2;
                next_position += 1
                tokens.append([current_token, current_state])           # token list contains token and its end state
                current_state = "0"                         
                current_token = ""                        
                continue
            case None:          # Cut the token and save when find next state of states that dont appear in table (end state)
                tokens.append([current_token, current_state])
                current_state = "0"
                current_token = ""
                next_position += 1
                continue
            case _:             # All state that can be follower by another state
                if (current_state not in ["86", "83"]) and (next_char in utils.whitespaces or next_char in utils.new_line):        # skip and create new token when meet an whitespaces and newline outside "" and /**?
                    next_position += 1
                    tokens.append([current_token, current_state])
                    current_state = "0"
                    current_token = ""
                    continue
                current_token = current_token + next_char
                current_state = next_state
                next_position += 1
                continue

    tokens = list(filter(lambda a: a[0] != "", tokens))  # Remove token create bt string of whitespace and newline
    # Write the tokens to a file.
    utils.write_tokens(tokens)       
