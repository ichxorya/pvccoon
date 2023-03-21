# Import libraries.
import csv

# Utils class
class Utils:
    # __init__(self, path: str): Initialize the utils.
    def __init__(self, path: str):
        # Read the transition table.
        self.data = list(csv.reader(open("transition_table.dat")))

        # Get the maps.
        self.map_state, self.map_key = self.get_maps(self.data)

        # Get the source code.
        self.source_code = self.get_source_code(path)

        # Whitespaces list.
        self.whitespaces = [" ", "\t"]

        # New lines list.
        self.new_lines = ["\r", "\n", "\r\n"]

    # get_input(self, path: str): Get the the source code as a string.
    def get_source_code(self, path: str):
        # Read the source code.
        with open(path, "r") as file:
            # Return the source code.
            return file.read()

    # get_maps(self, data: list): Get the maps for states and keys.
    def get_maps(self, data: list):
        # Initialize the maps
        map_state = {}  # Map for states (row)
        map_key = {}  # Map for keys (column)

        # Insert to map_state
        for i in range(
            len(data)
        ):  # len(table) = number of row && table format is 1...n as csv not 0.
            map_state[data[i][0]] = i

        # Insert to map_key
        for i in range(
            len(data[0])
        ):  # len(table[1]) = number of column && table format is 1...n as csv not 0,,n
            map_key[data[0][i]] = i

        return (map_state, map_key)

    # get_next_state(self, state: str, key: str): Get the next state from the current state and some input (key).
    def get_next_state(self, state: str, key: str):
        # Get the value
        try:
            # Special cases.
            if key in self.whitespaces:
                key = "Whitespace"
            elif key in self.new_lines:
                key = "Newline"
            
            print(f"State: {state}, Key: {key} -> {self.data[self.map_state[state]][self.map_key[key]]}")
            
            return self.data[self.map_state[state]][self.map_key[key]]
        except:
            return ""

    # write_tokens(self, tokens: list): Write the tokens to a file.
    def write_tokens(self, tokens: list):
        # Write the tokens to a file.
        with open("tokens.vctok", "w") as file:
            file.write("\n".join(tokens))

    # is_keyword(self, state: str): Check if the current state is a keyword.
    def is_keyword(self, state: str):
        try:
            return int(state) in [
                7,  # boolean
                11,  # break
                19,  # continue
                23,  # else
                28,  # false
                93,  # float
                30,  # for
                33,  # int
                89,  # if
                39,  # return
                43,  # true
                47,  # void
                52,  # while
            ]
        except:
            return False

    # is_separator(self, state: str): Check if the current state is a separator.
    def is_separator(self, state: str):
        try:
            return int(state) >= 69 and int(state) <= 76
        except:
            return False

    # is_operator_probably(self, state: str): Check if the current state is an operator (probably).
    def is_operator_probably(self, state: str):
        try:
            return int(state) >= 53 and int(state) <= 68
        except:
            return False

    # is_operator_single(self, state: str): Check if the current state is an operator (single-char).
    def is_operator_single(self, state: str):
        try:
            return int(state) in [
                53,  # +
                54,  # -
                55,  # *
                56,  # /
                57,  # =
                58,  # <
                59,  # >
                66,  # !
            ]
        except:
            return False

    # is_operator_double(self, cur_state: str, next_state: str): Check if the current state is an operator (double-char).
    def is_operator_double(self, cur_state: str, next_state: str):
        try:
            cur_state, next_state = int(cur_state), int(next_state)
            return (
                (cur_state == 57 and next_state == 67) # ==
                or (cur_state == 66 and next_state == 68) # !=
                or (cur_state == 57 and next_state == 60) # <=
                or (cur_state == 57 and next_state == 61) # >=
                or (cur_state == 62 and next_state == 64) # &&
                or (cur_state == 63 and next_state == 65) # ||
            )
        except:
            return False
        
    # is_number(self, state: str): Check if the current state is a number.
    def is_number(self, state: str):
        try:
            return int(state) == 77
        except:
            return False
