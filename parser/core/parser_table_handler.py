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
        # Read data from the CSV file and convert it into a list.
        self.lst = list(csv.reader(open(sourceCsv)))

        # Split the second and third elements of each row into separate lists.
        for i in self.lst:
            i[1] = i[1].split()
            i[2] = i[2].split()

        # Add a row to the end of the table with predefined values.
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
        # Iterate over each row in the table.
        for i in self.lst:
            # Check if the current state and token match the row's state and token values.
            if curState == i[0] and token in i[2]:
                # Return the next state associated with the current state and token.
                return i[1]

        # If no matching state and token pair is found, return "error".
        return "error"

    def printlst(self):
        """Prints the table data."""
        # Iterate over each row in the table and print it, along with a newline.
        for i in self.lst:
            print(f"{i}\n")
