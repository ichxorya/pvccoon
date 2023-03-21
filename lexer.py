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
        # Initialize the current token.
        current_token = ""

        # Get the current character.
        current_char = source_code[current_position]

        # Get the next character.
        if current_position + 1 < len(source_code):
            next_char = source_code[current_position + 1]
        else:
            next_char = ""

        # Get the next state (from the state 0, with the current character as input)
        next_state = utils.get_next_state("0", current_char)

        # Exit if the state is error.
        if next_state == "69420":
            print(f"Error: Error state reached, position {current_position}.")
            sys.exit(1)

        # If the current character is a whitespace/new line, skip it.
        if current_char in utils.whitespaces or current_char in utils.new_lines:
            current_position += 1
            continue

        # If the current character is a separator, add it to the tokens.
        if utils.is_separator(next_state):
            tokens.append(current_char)
            current_position += 1
            continue

        # If the current character is a operator...
        if utils.is_operator_probably(next_state):
            # Next of next state.
            next_next_state = utils.get_next_state(next_state, next_char)

            # If the next character is not-probably an operator...
            if utils.is_operator_probably(next_next_state) == False:
                # If the current character is a operator, add it to the tokens.
                if utils.is_operator_single(next_state):
                    tokens.append(current_char)
                    current_position += 1
                    continue
                else:
                    # Exit with the error with single '&' and '|'.
                    print(
                        f"Error: The {current_char} should be {current_char + current_char}, position {current_position}."
                    )
                    sys.exit(1)
            else:
                # If the next character is an operator, add it to the current token.
                if utils.is_operator_double(next_state, next_next_state):
                    current_token += current_char + next_char
                    tokens.append(current_token)
                    current_position += 2
                    continue
                
        # If the current character is a number...
        if utils.is_number(next_state):
            # While the next state is a number...
            while utils.is_number(next_state):
                # Add the current character to the current token.
                current_token += current_char

                # Get the next character.
                current_position += 1
                if current_position < len(source_code):
                    current_char = source_code[current_position]
                else:
                    break

                # Get the next state.
                next_state = utils.get_next_state(next_state, current_char)

            # Add the current token to the tokens.
            tokens.append(current_token)

        # Update position.
        current_position += 1
    
    # End of file.
    tokens.append("$")

    # Write the tokens to a file.
    utils.write_tokens(tokens)
