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
        if next_state == "69420": # Error state.
            print("ERROR")
            sys.exit(1)

        # If current character is a whitespace/new line, skip it.
        if current_char in utils.whitespaces or current_char in utils.new_line:
            current_position += 1
            continue

        # If current character is a separator, add it to the tokens.
        if current_char in utils.separators:
            tokens.append(current_char)
            current_position += 1
            continue
            
        # If current character is a letter, check if it is a keyword.
        if current_char.isalpha():
            # While the next state is available, run until the next state is not available.
            while next_state != "" and next_state != "69420":
                # Update the current state and token.
                current_state = next_state
                current_token += current_char
                current_position += 1
                print(current_token)
                print(current_state)

                # Get the next character.
                if current_position + 1 < len(source_code):
                    next_char = source_code[current_position + 1]
                else:
                    next_char = ""

                # Get the next state.
                next_state = utils.get_next_state(current_state, next_char)
                current_char = next_char
            # If the current state is a keyword, add it to the tokens.
            if utils.is_keyword(current_state):
                tokens.append(current_token)
            else:
                tokens.append("identifier")


        current_position += 1
        current_token = ""

    # Write the tokens to a file.
    utils.write_tokens(tokens)       
