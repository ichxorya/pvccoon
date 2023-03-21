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

    current_position = 0
    next_position = 0

    # Loop through the source code.
    while current_position < len(source_code):
        # Get the current character.
        current_char = source_code[current_position]

        # Get the next character.
        if current_position + 1 < len(source_code):
            next_char = source_code[current_position + 1]
        else:
            next_char = ""

        # Reset the current state.
        current_state = "0"

        # Get the next state.
        next_state = utils.get_next_state(current_state, current_char)
        
        # Exit if the state is error.
        if next_state == "69420":
            print("ERROR")
            sys.exit(1)

        # If the current character is a whitespace/new line, skip it.
        if current_char in utils.whitespaces or current_char in utils.new_line:
            current_position += 1
            continue

        # If the current character is a separator, add it to the tokens.
        if utils.is_separator(next_state):
            tokens.append(current_char)
            current_position += 1
            continue
        
        # If the current character is a operator...
        if utils.is_operator_probably(next_state):
            pass

        current_position += 1
        current_token = ""

    # Write the tokens to a file.
    utils.write_tokens(tokens)       
