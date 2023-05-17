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
        if self.type == "NONTERM":
            return self.branch[0]
        else:
            str = ""
            for i in self.branch:
                str += i.printTree()
            return str

class LParser:
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
    def isTerminal(self, str):
        return str in self.termLst
    
    def __init__(self, filePath) -> AST:
        self.tab = TableHandleClass("grammar.csv")
        self.tokenLst = clean_lexer_token("token_rules.lark", filePath)

    def parse2Ll1(self):
        i = 0
        stk = ["$", "PROGRAM"]
        while stk:
            x = stk[-1]
            a = self.tokenLst[i]
            print(x, " ",self.isTerminal(x.upper()), " ",a.type, " ",a.value)
            if self.isTerminal(x.upper()):
                if x == self.termLst[a.type]:
                    stk.pop()
                    i = i + 1 
                    print("terminal")
                else:
                    print("error")                    
            else:
                next = self.tab.getNextState(x, self.termLst[a.type])
                print(next)
                if next == "error":
                    print("error-non")
                else:
                    next = list(reversed(next))
                    stk.pop()
                    for j in next:
                        stk.append(j)
                    print("nonterminal")

            print(stk)
            print(i)
            print()
        print("done")
    