class Product:
    def __init__(self, pChoice, repeat = 1):
        self.pChoice = pChoice
        self.repeat = repeat

class Terminal:
    def __init__(self, terminal, repeat = 1):
        self.terminal = terminal
        self.repeat = repeat

class Tree:
    def __init__(self, name):
        self.lst = []
        self.name = name

    def addBranch(self, brch):
        self.lst.append(brch)

    def printTree(self):
        str = self.name + "\n"
        if len(self.lst) != 0:
            for i in self.lst:
                str += i.printTree() + "\n"
        return str