from TableHandle import TableHandleClass
from lexerToken import clean_lexer_token
import re

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
                    str = str[:len(str) - 1]    
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
                str = str[:len(str) - 1]
                if self.type in ["STMT", "SUBCOMPOUNDSTMT2"]:
                    str += "\n"
            return str
    
    def prettier(self):
        count = 0
        mod = ""
        output = self.printTree()
        output = output.replace("\n ", "\n")
        output = re.sub("\n+", "\n", output)
        output = re.sub(r"\(\s*", "(", output)
        output = re.sub(r"\s*\)", ")", output)
        output = re.sub(r"\s*\;", ";", output)
        #modified_string = ""
        #for char in output:
        #    if char == "\n":
        #        modified_string += " "  # replace newline with space
        #    else:
        #        modified_string += char  # keep other characters unchanged
        return output

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
        tab = TableHandleClass("grammar.csv")
        tokenLst = clean_lexer_token("token_rules.lark", filePath)

        def rec_parser(state, index):
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
                            nonterm, i = rec_parser(j, i)
                            if nonterm.type != "Empty":
                                ret.addTree(nonterm)
                    else:
                        ret = AST(state, "Empty")
                    return ret, i

        tree, i = rec_parser("PROGRAM", 0)
        return tree.prettier()
