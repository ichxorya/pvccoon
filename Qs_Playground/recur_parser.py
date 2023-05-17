from TableHandle import TableHandleClass
from lexerToken import clean_lexer_token

class AST:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.branch = []
    def addTree(self, tree):
        self.branch.append(tree)
    def printTree(self):
        if self.type == "Terminal":
            print(self.branch[0])
        else:
            str = ""
            for i in self.branch:
                str += i.printTree() + " "
            print(str)

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
    "$":"$"
}

def isTerminal(str):
        return str in termLst

def ast_builder(filePath):
    tab = TableHandleClass("grammar.csv")
    tokenLst = clean_lexer_token("token_rules.lark", filePath)

    def rec_parser(state, index):
        if isTerminal(state.upper()):
            if state == termLst[tokenLst[index].type]:
                ret = AST(state, "Terminal")
                ret.addTree(tokenLst[index].value)
                print(tokenLst[index].value, " ", index)
                return ret, index + 1
            else:
                print("error")                    
        else:
            next = tab.getNextState(state, termLst[tokenLst[index].type])
            print(next)
            if next == "error":
                print("error-non")
                return
            else:
                next = list(next)
                ret = AST(state, "NonTerminal")
                i = index
                for j in next:
                    nonterm, i = rec_parser(j, i)
                    print(j, " ", i)
                    ret.addTree(nonterm)
                return ret, i

    tree = rec_parser("PROGRAM", 0)
    tree.printTree()