from lark import Lark, Token


def lexer_token(rule_path, file_path):
    """
    Performs lexical analysis on the code file using the specified rule file.

    Args:
        rule_path (str): The path to the rule file.
        file_path (str): The path to the code file.

    Returns:
        list: A list of Token objects representing the analyzed code.
    """
    rule = open(rule_path, "r").read()  # Open rule file

    vc_parser = Lark(rule)  # Create Lark parser

    prog = open(file_path, "r").read()  # Open code file

    lex_iter = vc_parser.lex(prog)  # Create a generator of Token list

    lst = list(lex_iter)  # Transform generator to normal list

    lst.append(Token("$", "$"))  # Add end-of-file token

    return lst


def clean_lexer_token(rule_path, file_path):
    """
    Cleans the list of Tokens by removing whitespace and comment Tokens.

    Args:
        rule_path (str): The path to the rule file.
        file_path (str): The path to the code file.

    Returns:
        list: A cleaned list of Token objects.
    """
    tokens = lexer_token(rule_path, file_path)
    cleaned_tokens = []
    for token in tokens:
        if token.type not in ["WHITESPACES", "COMMENT"]:
            cleaned_tokens.append(token)
    return cleaned_tokens
