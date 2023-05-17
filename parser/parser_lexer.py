from lark import Lark, Token


# Create a list of Token
def lexer_token(rule_path, file_path):
    rule = open(rule_path, "r").read()  # Open rule file

    vc_parser = Lark(rule)  # Create Lark

    prog = open(file_path, "r").read()  # Open code file

    lex_iter = vc_parser.lex(prog)  # Create a generator made of list of Token

    lst = list(lex_iter)  # Transform generator to normal list

    lst.append(Token("$", "$"))

    return lst


def clean_lexer_token(rule_path, file_path):
    temp = lexer_token(rule_path, file_path)
    ret = []
    for i in temp:
        if i.type not in ["WHITESPACES", "COMMENT"]:
            ret.append(i)
    return ret
