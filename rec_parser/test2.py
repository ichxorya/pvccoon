from TableHandle import TableHandleClass
from lparser import LParser
from recur_parser import AST

#tab = TableHandleClass("grammar.csv")

#tab.printlst()

#print(tab.getNextState("PROPERPARALIST", "rparen"))

#test = LParser("example_fib.vc")
#test.parse2Ll1()

test = AST()
rule = open("output.vcps","w").write(test.ast_builder("example_fib.vc")) 