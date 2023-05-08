from Production import Product
from Production import Terminal
from Production import Tree
from grammar import grammarTable

from lark import Lark

# Create a list of Token
def lexer_token(rule_path, file_path):
    rule = open(rule_path,"r").read()           # Open rule file

    vc_parser = Lark(rule)                      # Create Lark

    prog = open(file_path, "r").read()          # Open code file

    lex_iter = vc_parser.lex(prog)              # Create a generator made of list of Token

    lst = list(lex_iter)                        # Transform generator to normal list

    return lst      

#test = lambda rule_path, file_path: list(Lark(open(rule_path,"r").read()).lex(open(file_path, "r").read()))         # One-line code

test = lexer_token("token_rules.lark", "example_fib.vc")

ret = ""
for i in test:
    if i.type not in ["WHITESPACES", "COMMENT"]:
        ret += i.type + " " + i.value + "\n"

out = open("output.txt", 'w').write(ret)

def ast_maker(tokenLst):    
    loc = 0
    token = tokenLst[loc]       
    
    error = "there's error!"

    def searchProduct(str):
        for i in grammarTable:
            if [str == i[0]]:
                return grammarTable.index(i)
        return -1

    def checkNode(product):
        tree = Tree(product)
        count = 1
        while count < len(product):
            i = product[count]
            if isinstance(i, Product): 
                check = False
                for j in i.pChoice:
                    ret = checkNode(grammarTable[searchProduct(j)])
                    if ret != error:
                        check = True
                        tree.addBranch(ret)
                        break
                if check == False:
                    if i.repeat == "1":
                        return error
                else:
                    loc += 1
                    token = tokenLst[loc]
                    if i.repeat == "n":
                        i -= 1
                
            elif isinstance(i, Terminal): 
                if i.terminal.count(token.type) > 0:
                    tree.addBranch(Tree(token.value))
                    loc += 1
                    token = tokenLst[loc]
                else:
                    if i.repeat == "1":
                        return error
            elif isinstance(i, str):
                ind = searchProduct(i)
                if ind >= 0:
                    ret = checkNode(grammarTable[ind])
                    if ret == error:
                        return error
                    else:
                        tree.addBranch(ret)
                        loc += 1
                        token = tokenLst[loc]
                else:
                    if token.value == i:
                        tree.addBranch(Tree(i))
                        loc += 1
                        token = tokenLst[loc]
                    else:
                        return error
            else:
                return error
            i += 1
        return tree
    
    return checkNode("program")

ast_maker(test).printTree()


