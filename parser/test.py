from parser_ast import AST

test = AST()
rule = open("output.vcps","w").write(test.ast_builder("example.vc"))