from table_test import ParsingTable

class LL1Parser:
    def __init__(self, parsing_table):
        self.table = parsing_table

    def parse(self, expression):
        stack = ['$']  # Start with end-of-input marker
        stack.append(self.table.start_symbol)

        tokens = expression.split()  # Split the expression into tokens

        f = open("log.txt", "w")

        while len(stack) > 0:
            top = stack[-1]
            lookahead = tokens[0] if tokens else '$'

            f.write("Stack: " + str(stack) + "\n")
            f.write("Lookahead: " + lookahead + "\n")
            f.write("Top: " + top + "\n")
            f.write("\n")

            if top == '$' and lookahead == '$':
                break

            if top in self.table.terminals:
                if top == lookahead:
                    stack.pop()
                    if tokens:
                        tokens.pop(0)
                else:
                    raise Exception("Error: Unexpected token")

            elif top in self.table.non_terminals:
                if self.table.get(top, lookahead):
                    stack.pop()
                    production = self.table.get(top, lookahead)
                    for symbol in reversed(production):
                        stack.append(symbol)

                else:
                    raise Exception("Error: Invalid production")

            else:
                raise Exception("Error: Invalid symbol: " + top + "\nStack" + str(stack))

            if len(stack) > 390000:
                # Time out
                raise Exception("Error: Time out")

        if len(tokens) == 0:
            print("Parsing successful!")
        else:
            print("Parsing failed!")

table = ParsingTable('table.dat')
parser = LL1Parser(table)

parser.parse("bird")
parser.parse("big big bird")
parser.parse("big big big bird")
parser.parse("big big big big bird")

# These throw an exception:
# parser.parse("big big big big big bird bird")
# parser.parse("")
# parser.parse("big")
# parser.parse("big big big big big big big")
