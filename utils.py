# Import libraries.
import csv

# Utils class
class Utils:
    def __init__(self, path: str):
        # Read the transition table.
        self.data = list(csv.reader(open("transition_table.dat")))

        # Get the maps.
        self.map_state, self.map_key = self.get_maps(self.data)

        # Get the source code.
        self.source_code = self.get_source_code(path)

        # Keyword list.
        self.keywords = [
            "boolean",
            "break",
            "continue",
            "else",
            "false",
            "float",
            "for",
            "if",
            "int",
            "return",
            "true",
            "void",
            "while",
        ]

        # Separator list.
        self.separators = ["(", ")", "{", "}", "[", "]", ";", ","]

        # Whitespaces list.
        self.whitespaces = [" ", "\t"]

        # New line list.
        self.new_line = ["\r", "\n", "\r\n"]

    # get_input(path: str): Get the the source code as a string.
    def get_source_code(self, path: str):
        # Read the source code.
        with open(path, "r") as file:
            # Return the source code with left strip and right strip.
            return file.read()

    # get_maps(data): Get the maps for states and keys.
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

    # get_next_state(data, state, key): Get the next state from the current state and some input (key).
    def get_next_state(self, state, key):
        # Get the value
        try:
            return self.data[self.map_state[state]][self.map_key[key]]
        except:
            return ""
        
    # write_tokens(tokens: list): Write the tokens to a file.
    def write_tokens(self, tokens: list):
        # Write the tokens to a file.
        with open("tokens.vctok", "w") as file:
            output = ""
            for i in tokens:
                output = output + "{}\n".format(i[0])
            file.write(output)

    # write_verbose(tokens: list): Write the tokens to a file in verbose form
    def write_verbose(self, tokens: list):
        # Write the tokens to a file.
        with open("tokenverbose.vctok", "w") as file:
            output = "======= The VC compiler =======\n"
            for i in tokens:
                output = output + "State = {} [{}], spelling = \"{}\", position = {}({})..{}({})\n".format(i[1], self.find_type(i[1]) , i[0], i[2][0], i[2][1], i[3][0] ,i[3][1])
            file.write(output)
    
    # is_keyword(state: str): Check if the current state is a keyword.
    def is_keyword(self, state: str):
        # Check if the current state is a keyword.
        return state in [
            7, # boolean
            11, # break
            19, # continue
            23, # else
            28, # false
            93, # float
            30, # for
            33, # int
            89, # if
            39, # return
            43, # true
            47, # void
            52, # while
        ]

    def find_type(self, state):
        # Find the type from the state
        match state:
            case "999":
                return "$"
            case "78" | "79":
                return "<float-literal>"
            case "77":
                return "<int-literal>"
            case "84":
                return "<string-literal>"    
            case "6969" | "31" | "1"| "12" | "20" | "24" | "34" | "40" | "44" | "48":
                return "<id>"
            case "60":
                return "<="
            case "67":
                return "=="
            case "61":
                return ">="
            case "64":
                return "&&"
            case "65":
                return "||"
            case "60":
                return "!!"
            case "7":
                return "boolean"
            case "11":
                return "break"
            case "19":
                return "continue"
            case "23":
                return "else"
            case "28":
                return "false"
            case "93":
                return "float"
            case "30":
                return "for"
            case "33":
                return "int"
            case "89":
                return "if"
            case "39":
                return "return"
            case "43":
                return "true"
            case "47":
                return "void"
            case "52":
                return "while"
            case _:
                for i in range(len(self.data[1])):
                    if self.data[1][i] == state:
                        return self.data[0][i]