# Import libraries.
import sys, os
from parser_ast import AST

# Main function.
if __name__ == "__main__":
    # Check the arguments.
    if len(sys.argv) < 2:
        print("Usage: python parser.py <path>")
        print("Or: python parser.py --example (to parse the example .vc files)")
        sys.exit(1)

    arg = sys.argv[1]

    # Check if the user wants to parse the examples.
    if arg == "--example":
        # Get the .vc files from the examples folder (../example/).
        examples = os.listdir("../example/")
        examples = [i for i in examples if i.endswith(".vc")]
        print("* Parsing the following files:")
        for i in examples:
            print(f"---- {i}")

        # Create the parse tree.
        ast = AST()

        for i in examples:
            name = i.split(".")[0]
            rule = open(f"output/output_{name}.vcps", "w").write(
                ast.ast_builder(f"../example/{i}")
            )

        sys.exit(0)

    # Check if the user wants to parse a file.
    else:
        # Check if the file exists.
        try:
            open(arg)
        except FileNotFoundError:
            print("File not found.")
            sys.exit(1)

        # Parse the file.
        ast = AST()
        name = arg.split(".")[0]
        rule = open(f"output/{name}.vcps", "w").write(ast.ast_builder(arg))
        print(f"* Parsing the file {arg}!")
        sys.exit(0)
