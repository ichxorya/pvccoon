from recur_parser import AST

test = AST()
rule = open("output.vcps","w").write(test.ast_builder("example_fib.vc"))
