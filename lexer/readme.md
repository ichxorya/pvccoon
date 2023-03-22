# Readme

This is the lexer for the VC language.

## Dependencies

- Python 3.8 or higher.

## Usage

First, move into the `lexer` folder.

Dependends on your purpose, you can use the lexer in two ways:

1. Use the lexer indirectly through the `run_lexer.py` script.
This script allows you to run the lexer with a single command, while you need to provide the source code file path before running the script.

2. Use the lexer directly through the `core/lexer.py` script.
This script allows you to run the lexer directly, but you need to provide the source code file path when you run the script.

```bash
# Run the lexer indirectly
python run_lexer.py

# Run the lexer directly
python core/lexer.py <path>
```

## Output

The lexer will generate two output files in the `output` folder:

- `token.vctok`: Contains the list of tokens extracted from the source code.
- `token.verbose.vctok`: Contains verbose information of the tokens, such as state, token type, spelling, and position.
