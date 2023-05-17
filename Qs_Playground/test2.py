from TableHandle import TableHandleClass
from lparser import LParser
from recur_parser import ast_builder

#tab = TableHandleClass("grammar.csv")

#tab.printlst()

#print(tab.getNextState("PROPERPARALIST", "rparen"))

#test = LParser("example_fib.vc")
#test.parse2Ll1()

ast_builder("example.vc")