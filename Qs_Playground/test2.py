from TableHandle import TableHandleClass

tab = TableHandleClass("data.csv")

tab.printlst()

print(tab.getNextState("A", "c"))