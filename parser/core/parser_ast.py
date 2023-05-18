from parser_table_handler import TableHandler
from parser_lexer import clean_lexer_token


class AST:
    """
    The AST class is used to build the abstract syntax tree.

    Attributes:
        name (str): The name of the node.
        type (str): The type of the node.
        branch (list): A list of the node's children (subtrees).
        exprLst (list): A list of some non-terminals (EXPRs).
        subexprLst (list): A list of some non-terminals (SUBEXPRs).
        termLst (dict): A list of the terminals.

    Methods:
        __init__(name, type): Initializes an AST node.
        addTree(tree): Adds a child to the node.
        printTree(): Prints the tree.
        ast_builder(source): Builds the AST.
        isTerminal(token): Checks if a token is a terminal.
        tab_helper(counter): A helper method to create strings of "\t" for decoration.
    """

    def __init__(self, name="", type=""):
        """
        Initializes an AST node.

        Args:
            name (str): The name of the node.
            type (str): The type of the node.
        """
        self.name = name
        self.type = type
        self.branch = []

        self.exprLst = [
            "ASSIGNMENTEXPR",
            "CONDOREXPR",
            "CONDANDEXPR",
            "EQUALITYEXPR",
            "RELEXPR",
            "ADDITIVEEXPR",
            "MULTIPLICATIVEEXPR",
            "UNARYEXPR",
        ]

        self.subexprLst = [
            "SUBASSIGNMENTEXPR",
            "SUBCONDOREXPR",
            "SUBCONDANDEXPR",
            "SUBEQUALITYEXPR",
            "SUBRELEXPR",
            "SUBADDITIVEEXPR",
            "SUBMULTIPLICATIVEEXPR",
        ]

        self.termLst = {
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

    def addTree(self, tree):
        """
        Adds a subtree to the current node.

        Args:
            tree (AST): The subtree to be added.
        """
        self.branch.append(tree)

    def tab_helper(self, counter):
        """
        A helper method to create strings of "\t" for decoration.

        Args:
            counter (int): The number of "\t" need to add.

        Returns:
            str: The string of "\t".
        """
        str = ""
        i = 0
        while i < counter:
            i += 1
            str += "    "
        return str

    def printTree(self, tabCount):
        """
        Prints the tree starting from the current node.

        Args:
            tabCount (int): The number of "\t" for current token, use for decoration.

        Returns:
            str: The string representation of the tree.
        """

        # Print the value of terminal token.
        if self.type == "Terminal":
            # Special case: "else" token.
            if self.branch[0] == "else":
                str = self.tab_helper(tabCount)
                str = str[: len(str) - 1] + self.branch[0]
                return str
            # Normal token return their value.
            else:
                return self.branch[0]
        # Print the nonterminal token.
        else:
            # Special case: token "PROGRAM".
            if self.type == "PROGRAM":
                str = ""
                for i in self.branch:
                    j = i.printTree(tabCount)
                    # Special case: token "SUBPROGRAM", require "\n" between "SUBPROGRAM".
                    if i.type == "SUBPROGRAM":
                        str += j + "\n"
                    else:
                        str += j + " "
                str = str[: len(str) - 1]
            # Special case: token "COMPOUNDSTMT", use tab_helper() to decorate program.
            elif self.type == "COMPOUNDSTMT":
                str = "\n"
                for i in self.branch:
                    j = i.printTree(tabCount)
                    if j != "":
                        if j == "{":
                            str += self.tab_helper(tabCount) + j + "\n"
                        elif j == "}":
                            str += self.tab_helper(tabCount) + j
                        else:
                            str += j
            # Special case: token "STMT" and "SUBCOMPOUNDSTMT2", add "\n" after each stament or declaration.
            elif self.type in ["STMT", "SUBCOMPOUNDSTMT2"]:
                tabCount += 1
                str = self.tab_helper(tabCount)
                for i in self.branch:
                    j = i.printTree(tabCount)
                    if j != "":
                        str += j + " "
                str += "\n"
            # Special case: token "SUBCOMPOUNDSTMT", print stament or declaration continuously.
            elif self.type == "SUBCOMPOUNDSTMT":
                str = ""
                for i in self.branch:
                    j = i.printTree(tabCount)
                    if j != "":
                        str += j
            # Special case: children of token "EXPR",
            # print child token if there is only 1 child,
            # print token inside ( ) if there are more children.
            elif self.type in self.exprLst:
                if len(self.branch) == 1:
                    str = ""
                    j = self.branch[0].printTree(tabCount)
                    if j != "":
                        str += j
                else:
                    str = "("
                    for i in self.branch:
                        j = i.printTree(tabCount)
                        if j != "":
                            str += j
                    str = str[: len(str) - 1]
                    str += ")"
            # Special case: children of children of token "EXPR",
            # print with or without ( ) depend on number of children.
            elif self.type in self.subexprLst:
                if len(self.branch) == 3:
                    str = (
                        " "
                        + self.branch[0].printTree(tabCount)
                        + " ("
                        + self.branch[1].printTree(tabCount)
                        + self.branch[2].printTree(tabCount)
                        + ")"
                    )
                else:
                    str = (
                        " "
                        + self.branch[0].printTree(tabCount)
                        + " "
                        + self.branch[1].printTree(tabCount)
                        + ")"
                    )
            # Normal case: print children token, separate by " ".
            else:
                str = ""
                for i in self.branch:
                    j = i.printTree(tabCount)
                    if j != "":
                        str += j + " "
                str = str[: len(str) - 1]
            return str

    def isTerminal(self, str):
        """
        Checks if a string represents a terminal.

        Args:
            str (str): The string to check.

        Returns:
            bool: True if the string represents a terminal, False otherwise.
        """
        return str in self.termLst

    def ast_builder(self, filePath):
        """
        Builds an Abstract Syntax Tree (AST) from the given file path.

        Args:
            filePath (str): The path to the file containing the tokens.

        Returns:
            str: The prettified code represented by the AST.
        """
        # Load the parsing table (grammar.dat) and the tokens (using the lexer).
        tab = TableHandler("grammar.dat")
        tokenLst = clean_lexer_token("token_rules.lark", filePath)

        # Initialize the AST in terms of a recursive parser.
        def recursive_parser(state, index):
            """
            Builds an Abstract Syntax Tree (AST) recursively at current state.

            Args:
                state (str): The curent state to build AST.
                index the curent token index in token list.

            Returns:
                (ret, i): tuple
                    ret: The AST of current state.
                    i: the index after parsing though state
            """
            # IF token is terminal
            if self.isTerminal(state.upper()):
                # if the value of token match the terminal in grammar.
                if state == self.termLst[tokenLst[index].type]:
                    # Create AST of current token and add the value as its child.
                    ret = AST(state, "Terminal")
                    ret.addTree(tokenLst[index].value)
                    # return the AST, move the index to next token
                    return ret, index + 1
                # return "error" if the value is unmatch.
                else:
                    print("error")
            # IF token is nonterminal
            else:
                # Get the list of token as result of production.
                next = tab.getNextState(state, self.termLst[tokenLst[index].type])
                # return "error" if no production is found.
                if next == "error":
                    return "error"
                else:
                    next = list(next)
                    i = index
                    # Create normal AST if result of production is not empty.
                    if len(next) > 0:
                        ret = AST(state, state)
                        for j in next:
                            nonterm, i = recursive_parser(j, i)
                            # Ignore empty AST.
                            if nonterm.type != "Empty":
                                ret.addTree(nonterm)
                    # Create empty AST if result of production is empty.
                    else:
                        ret = AST(state, "Empty")
                    return ret, i

        tree, _ = recursive_parser("PROGRAM", 0)
        # Print error if cannopt build ASST.
        if tree == "error":
            print("Cannot parse with program: Program grammar is not VC.")
        return tree.printTree(0)
