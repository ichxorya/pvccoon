from parser_table_handler import TableHandler
from parser_lexer import clean_lexer_token
import re, subprocess


class AST:
    def __init__(self, name="", type=""):
        self.name = name
        self.type = type
        self.branch = []

    def addTree(self, tree):
        self.branch.append(tree)

    def tab_helper(self, counter):
        str = ""
        i = 0
        while i < counter:
            i += 1
            str += "    "
        str = str[: len(str) - 1]
        return str

    def printTree(self):
        if self.type == "Terminal":
            return self.branch[0]
        else:
            if self.type in self.parenttypeLst:
                if len(self.branch) == 1:
                    j = self.branch[0].printTree()
                    if j != "":
                        str = j
                    else:
                        str = ""
                else:
                    str = "("
                    for i in self.branch:
                        j = i.printTree()
                        if j != "":
                            if j in ["{", "}"]:
                                str += "\n" + j + "\n"
                            elif j == ";":
                                str += j + "\n"
                            else:
                                str += j + " "
                    str = str[: len(str) - 1]
                    str += ")"
            else:
                str = ""
                for i in self.branch:
                    j = i.printTree()
                    if j in ["{", "}"]:
                        str += "\n" + j + "\n"
                    elif j == ";":
                        str += j + "\n"
                    else:
                        str += j + " "
                str = str[: len(str) - 1]
                if self.type in ["STMT", "SUBCOMPOUNDSTMT2"]:
                    str += "\n"
            return str

    def prettify(self):
        output = self.printTree()
        output = output.replace("\n ", "\n")
        output = re.sub("\n+", "\n", output)
        output = re.sub(r"\(\s*", "(", output)
        output = re.sub(r"\s*\)", ")", output)
        output = re.sub(r"\s*\;", ";", output)

        return self.prettify2(output)

    def prettify2(self, code):
        # Remove unnecessary whitespace.
        code = code.replace("\n", " ").replace("\r", "")

        # Add indentation.
        indentation = 0
        formatted_code = ""
        for char in code:
            if char == "{":
                formatted_code += (
                    "\n" + " " * indentation + char + "\n" + " " * (indentation + 2)
                )
                indentation += 2
            elif char == "}":
                indentation -= 2
                formatted_code += "\n" + " " * indentation + char
            else:
                formatted_code += char

        return self.prettify3(formatted_code)

    def prettify3(self, code):
        INDENT_SIZE = 2  # Number of spaces for each indentation level

        # Split the code into lines
        lines = code.split("\n")

        # Initialize variables
        indent_level = 0
        prettified_code = ""

        # Iterate through each line
        for line in lines:
            line = line.strip()  # Remove leading/trailing whitespace

            # Skip empty lines
            if not line:
                continue

            # Adjust the indentation level based on opening/closing braces
            if line.startswith("}"):
                indent_level -= 1

            # Add indentation to the line
            prettified_line = " " * (INDENT_SIZE * indent_level) + line

            # Append the prettified line to the result
            prettified_code += prettified_line + "\n"

            # Adjust the indentation level based on opening/closing braces
            if line.endswith("{"):
                indent_level += 1

        return self.prettify4(prettified_code)

    def prettify4(self, code):
        # Write the code to a temporary file.
        with open("temp.vcps", "w") as file:
            file.write(code)

        # Define the command.
        command = "c_formatter_42 < temp.vcps"

        # Execute the command in the Command Prompt
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Load the result into a string.
        formatted_code = result.stdout

        # Remove the temporary file.
        subprocess.run("del temp.vcps", shell=True)

        return formatted_code

    parenttypeLst = [
        "ASSIGNMENTEXPR",
        "CONDOREXPR",
        "CONDANDEXPR",
        "EQUALITYEXPR",
        "RELEXPR",
        "ADDITIVEEXPR",
        "MULTIPLICATIVEEXPR",
    ]
    termLst = {
        "IDENTIFIER": "identifier",
        "IF": "if",
        "ELSE": "else",
        "FOR": "for",
        "WHILE": "while",
        "BREAK": "break",
        "CONTINUE": "CONTINUE",
        "RETURN": "return",
        "VOID": "void",
        "FLOAT": "float",
        "INT": "int",
        "BOOLEAN": "boolean",
        "INTLITERAL": "intliteral",
        "FLOATLITERAL": "floatliteral",
        "BOOLLITERAL": "boolliteral",
        "STRINGLITERAL": "stringliteral",
        "PLUS": "plus",
        "MINUS": "minus",
        "STAR": "star",
        "SLASH": "slash",
        "LT": "lt",
        "GT": "gt",
        "LTE": "lte",
        "GTE": "gte",
        "EQ": "eq",
        "NEQ": "neq",
        "AND": "and",
        "OR": "or",
        "NOT": "not",
        "ASSIGN": "assign",
        "COMMA": "comma",
        "SEMICOLON": "semicolon",
        "LPAREN": "lparen",
        "RPAREN": "rparen",
        "LBRACE": "lbrace",
        "RBRACE": "rbrace",
        "LBRACKET": "lbracket",
        "RBRACKET": "rbracket",
        "$": "$",
    }

    def isTerminal(self, str):
        return str in self.termLst

    def ast_builder(self, filePath):
        tab = TableHandler("grammar.dat")
        tokenLst = clean_lexer_token("token_rules.lark", filePath)

        def recursive_parser(state, index):
            if self.isTerminal(state.upper()):
                if state == self.termLst[tokenLst[index].type]:
                    ret = AST(state, "Terminal")
                    ret.addTree(tokenLst[index].value)
                    return ret, index + 1
                else:
                    print("error")
            else:
                next = tab.getNextState(state, self.termLst[tokenLst[index].type])
                if next == "error":
                    return "error"
                else:
                    next = list(next)
                    i = index
                    if len(next) > 0:
                        ret = AST(state, state)
                        for j in next:
                            nonterm, i = recursive_parser(j, i)
                            if nonterm.type != "Empty":
                                ret.addTree(nonterm)
                    else:
                        ret = AST(state, "Empty")
                    return ret, i

        tree, i = recursive_parser("PROGRAM", 0)
        return tree.prettify()
