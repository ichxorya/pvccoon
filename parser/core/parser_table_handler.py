import csv

class TableHandler:
    """
    A class for handling tables and performing operations on them.

    Attributes:
        lst (list): A list representing the table data.

    Methods:
        __init__(sourceCsv): Initializes the TableHandler object by reading data from a CSV file.
        getNextState(curState, token): Retrieves the next state based on the current state and token.
        printlst(): Prints the table data.
    """

    def __init__(self, sourceCsv):
        """
        Initializes the TableHandler object by reading data from a CSV file.

        Args:
            sourceCsv (str): The path to the CSV file containing the table data.
        """
        self.lst = list(csv.reader(open(sourceCsv)))
        for i in self.lst:
            i[1] = i[1].split()
            i[2] = i[2].split()
        self.lst.append(
            ["ULTIMATE", ["PROGRAM", "$"], ["void", "int", "float", "boolean"]]
        )

    def getNextState(self, curState, token):
        """
        Retrieves the next state based on the current state and token.

        Args:
            curState (str): The current state.
            token (str): The token representing the input.

        Returns:
            str: The next state.
        """
        for i in self.lst:
            if curState == i[0] and token in i[2]:
                return i[1]
        return "error"

    def printlst(self):
        """Prints the table data."""
        for i in self.lst:
            print(i)
            print()
