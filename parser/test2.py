from TableHandle import TableHandleClass
from lparser import LParser

#tab = TableHandleClass("grammar.csv")

#tab.printlst()

#print(tab.getNextState("PROPERPARALIST", "rparen"))

test = LParser("example_fib.vc")
test.parse2Ll1()