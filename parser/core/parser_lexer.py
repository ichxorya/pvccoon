from lark import Lark, Token


def lexer_token(rule_path, file_path):
    """
    Performs lexical analysis on the code file using the specified rule file.

    Args:
        rule_path (str): The path to the lexer's rule file.
        file_path (str): The path to the source code file.

    Returns:
        list: A list of Token objects representing the analyzed code.
    """
    # Open the lexer's rule file and read it.
    rule = open(rule_path, "r").read()

    # Create a Lark parser using the rule file.
    vc_parser = Lark(rule)

    # Open the source code file and read it.
    prog = open(file_path, "r").read()

    # Perform lexical analysis on the source code.
    lex_iter = vc_parser.lex(prog)

    # Convert the iterator to a list.
    lst = list(lex_iter)

    # Add a $ token to the end of the list.
    lst.append(Token("$", "$"))

    # Return the list of Tokens.
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
    # Get the list of Tokens.
    tokens = lexer_token(rule_path, file_path)

    # Remove whitespace and comment Tokens.
    cleaned_tokens = []
    for token in tokens:
        if token.type not in ["WHITESPACES", "COMMENT"]:
            cleaned_tokens.append(token)

    # Return the cleaned list of Tokens.
    return cleaned_tokens
