import csv

class TableHandleClass:
    def __init__(self, sourceCsv):
        self.lst = list(csv.reader(open(sourceCsv)))
        for i in self.lst:
            i[1] = list(reversed(i[1].split()))
            i[2] = list(reversed(i[2].split()))
    def getNextState(self, curState, token):
        for i in self.lst:
            if (curState == i[0]) and (token in i[2]):
                return i[1]
        return "error"
    def printlst(self):
        for i in self.lst:
            print(i)
            print()

