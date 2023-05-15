class ParsingTable:
    def __init__(self, path):
        self.start_symbol, self.table = self.create_table(path)
        self.non_terminals = set(self.table.keys())
        self.terminals = set(
            terminal
            for terminals_and_productions in self.table.values()
            for terminal in terminals_and_productions.keys()
        )
        self.terminals.add('$')

    def create_table(self, path):
        start_symbol, table = self.parse_table(path)

        new_table = {}

        for non_terminal, terminals_and_productions in table.items():
            new_table[non_terminal] = {}

            for terminal, production in terminals_and_productions.items():
                new_table[non_terminal][terminal] = production
        return start_symbol, new_table

    def get(self, non_terminal, terminal):
        try:
            return self.table[non_terminal][terminal]
        except KeyError:
            return None

    def read_table(self, path):
        content = str(open(path).read())

        table_start = content.find('table')
        table_end = content.find('end_table')
        table_section = content[table_start:table_end]

        table_content = table_section.replace('table', '').replace('end_table', '').strip()

        #  Strip every line
        table_content = '\n'.join([line.strip() for line in table_content.split('\n')])

        return table_content

    def parse_table(self, path):
        content = self.read_table(path)

        table = {}

        for line in content.split('\n'):
            # If the line start with "start_symbol", then it is the start symbol
            if line.startswith('start_symbol'):
                # The start symbol is the first word after "start_symbol"
                start_symbol = line.split()[1]
                continue

            if line == '':
                continue

            non_terminal_and_terminal, production = line.split('->')

            non_terminal, terminal = non_terminal_and_terminal.split('and')
            non_terminal = non_terminal.strip()
            terminal = terminal.strip()

            production = [symbol.strip() for symbol in production.split()]

            if non_terminal not in table:
                table[non_terminal] = {}

            table[non_terminal][terminal] = production

        return start_symbol, table

# # Test
# table = ParseTable('table.dat')
# print(table.terminals)
# print(table.non_terminals)
# print(table.start_symbol)
# print(table.get('S', 'big'))  # Output: ['A', '$']
# print(table.get('S', 'bird'))  # Output: ['A', '$']
# print(table.get('A', 'big'))  # Output: ['big', 'A']
# print(table.get('A', 'bird'))  # Output: ['bird']
# print(table.get('A', '$'))  # Output: None


