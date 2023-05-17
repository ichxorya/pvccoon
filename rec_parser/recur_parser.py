from TableHandle import TableHandleClass
from lexerToken import clean_lexer_token


class AST:
    def __init__(self, name = "", type = ""):
        self.name = name
        self.type = type
        self.branch = []

    def addTree(self, tree):
        self.branch.append(tree)

    def printTree(self):
        if self.type == "Terminal":
            return self.branch[0]
        else:
            if self.type in self.parenttypeLst:
                if len(self.branch) == 1:
                    if self.type in ["$", "STMT"]:
                        str = "( "
                        j = self.branch[0].printTree()
                        if j != "":
                            str += j
                        str += " )"
                    else:
                        str = ""
                        j = self.branch[0].printTree()
                        if j != "":
                            str += j
                else:
                    str = "( "
                    for i in self.branch:
                        j = i.printTree()
                        if j != "":
                            str += j + " "
                    str = str[: len(str) - 1]
                    str += " )"
            else:
                str = ""
                for i in self.branch:
                    j = i.printTree()
                    if j != "":
                        str += j + " "
                str = str[: len(str) - 1]
            return str
    
    parenttypeLst = [
        "$",
        "PROGRAM",
        "SUBCOMPOUNDSTMT2",
        "STMT",
        "ASSIGNMENTEXPR",
        "CONDOREXPR",
        "CONDANDEXPR",
        "EQUALITYEXPR",
        "RELEXPR",
        "ADDITIVEEXPR",
        "MULTIPLICATIVEEXPR",
        "UNARYEXPR",
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

        tree, i = rec_parser("ULTIMATE", 0)
        return tree.printTree()
