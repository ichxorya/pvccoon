from Production import Product
from Production import Terminal

Terminal("")

program                     = ["program",                           Product(["func-decl", "var-decl"], "n")]

# declarations
funcdecl                    = ["func-decl",                         "type",         "identifier",           "para-list",            "compound-stmt"]
vardecl                     = ["var-decl",                          "type",         "init-declarator-list",             ";"]
initdeclaratorlist          = ["init-declarator-list",              "init-declarator",          Product(["sup-init-declarator-list"], "n")]
supinitdeclaratorlist       = ["sup-init-declarator-list",          ",",            "init-declarator"]
initdeclarator              = ["init-declarator",                   "declarator",       Product(["sup-init-declarator"], "op")]
supinitdeclarator           = ["sup-init-declarator",               "=",            "initialiser"]
declarator                  = ["declarator",                        "identifier",       Product(["sub-declarator"], "op")]
subdeclarator               = ["sub-declarator",                    "[",            ",",            Terminal("INTLITERAL", "op"),            "]"]
initialiser                 = ["initialiser",                       Product(["expr", "sub-initialiser"])]
subinitialiser              = ["sub-initialiser",                   "{",            "expr",         Product(["sub-sub-initialiser"], "n"),          "}"]
subsubinitialiser           = ["sub-sub-initialiser",               ",",            "expr"]                      


# primitive types
type                        = ["type",                              Terminal(["VOID", "BOOLEAN", "INT", "FLOAT"])]
# identifiers
identifier                  = ["identifier",                        Terminal("ID")]
# statements
compoundstmt                = ["compound-stmt",                     "{",            Product(["var-decl"], "n"),             Product(["stmt"], "n"),             "}"]
stmt                        = ["stmt",                              Product(["compound-stmt", "if-stmt", "for-stmt", "while-stmt", "break-stmt", "continue-stmt", "return-stmt", "expr-stmt"])]

ifstmt                      = ["if-stmt",                           Terminal("IF"),              "(",            "expr",             ")",            "stmt",         Product(["else-stmt"])]
elsestmt                    = ["else-stmt",                         Terminal("ELSE"),            "stmt"]

forstmt                     = ["for-stmt",                          Terminal("FOR"),             "(",            Product(["expr"], "op"),              ";",            Product(["expr"], "op"),          ";",            Product(["expr"], "op"),          ")",        "stmt"]                              
whilestmt                   = ["while-stmt",                        Terminal("WHILE"),           "(",            "expr",                             ")",            "stmt"]

breakstmt                   = ["break-stmt",                        Terminal("BREAK"),           ";"]
continuestmt                = ["continue-stmt",                     Terminal("CONTINUE"),        ";"]
                               
returnstmt                  = ["return-stmt",                       Terminal("RETURN"),          Product(["expr"], "op"),            ";"]
exprstmt                    = ["expr-stmt",                         Product(["expr"], "op"),            ";"]
                               
# expressions
expr                        = ["expr",                              "assignment-expr"]
assignmentexpr              = ["assignment-expr",                   Product(["sub-assignment-expr"], "n"),          "cond-or-expr"]
subassignmentexpr           = ["sub-assignment-expr",               "cond-or-expr",             "="]

condorexpr                  = ["cond-or-expr",                      Product(["cond-and-expr", "sub-cond-or-expr"])]
subcondorexpr               = ["sub-cond-or-expr",                  "cond-or-expr",             "||",               "cond-and-expr"]

condandexpr                 = ["cond-and-expr",                     Product(["equality-expr", "sub-cond-and-expr"])]
subcondandexpr              = ["sub-cond-and-expr",                 "cond-and-expr",            "&&",               "equality-expr"]

equalityexpr                = ["equality-expr",                     Product(["rel-expr", "equ-equality-expr", "non-equality-expr"])]
equequalityexpr             = ["equ-equality-expr",                 "equality-expr",            "==",               "rel-expr"]
nonequalityexpr             = ["non-equality-expr",                 "equality-expr",            "!=",               "rel-expr"]

relexpr                     = ["rel-expr",                          Product(["additive-expr", "less-rel-expr", "lesser-rel-expr" , "grwat-rel-expr" , "greater-rel-expr"])] 
lessrelexpr                 = ["less-equality-expr",                "rel-expr",                 "<",                "additive-expr"]
lesserrelexpr               = ["lesser-equality-expr",              "rel-expr",                 "<=",               "additive-expr"]
grwatrelexpr                = ["grwat-equality-expr",               "rel-expr",                 ">",                "additive-expr"]
greaterrelexpr              = ["greater-equality-expr",             "rel-expr",                 ">=",               "additive-expr"]


additiveexpr                = ["additive-expr",                     Product(["multiplicative-expr", "add-additive-expr", "sub-additive-expr"])]
addadditiveexpr             = ["add-additive-expr",                 "additive-expr",                "+",                "multiplicative-expr"]
subadditiveexpr             = ["sub-additive-expr",                 "additive-expr",                "-",                "multiplicative-expr"]

multiplicativeexpr          = ["multiplicative-expr",               Product(["unary-expr", "mul-multiplicative-expr", "div-multiplicative-expr"])]
mulmultiplicativeexpr       = ["mul-multiplicative-expr",           "multiplicative-expr",          "*",                "unary-expr"]
divmultiplicativeexpr       = ["div-multiplicative-expr",           "multiplicative-expr",          "/",                "unary-expr"]

unaryexpr                   = ["unary-expr",                        Product(["plus-unary-expr", "minus-unary-expr", "reverse-unary-expr", "primary-expr"])]
plusunaryexpr               = ["plus-unary-expr",                   "+",                "unary-expr"]
minusunaryexpr              = ["minus-unary-expr",                  "-",                "unary-expr"]
reverseunaryexpr            = ["reverse-unary-expr",                "!",                "unary-expr"]

primaryexpr                 = ["primary-expr",                      Product(["primary-expr1", "primary-expr2", "primary-expr3", "primary-expr-type"])]
primaryexprtype             = ["primary-expr_type",                 Terminal(["INTLITERAL", "FLOATLITERAL", "BOOLLITERAL", "STRINGLITERA"])]                            
primaryexpr1                = ["primary-expr1",                     "identifier",               Product(["arg-list"], "op")]
primaryexpr2                = ["primary-expr2",                     "identifier",               "[",                  ",",              "expr",             "]"]
primaryexpr3                = ["primary-expr3",                     "(",                        "expr",               ")"]

# parameters
paralist                    = ["para-list",                 "(",            Product(["proper-para-list"], "op"),        ")"]
properparalist              = ["proper-para-list",          "para-decl",    Product(["sub-proper-para-list"], "n")]
subproperparalist           = ["proper-para-list",          ",",            "para-decl"]
paradecl                    = ["para-decl",                 "type"          "declarator"]
arglist                     = ["arg-list",                  "(",            Product(["proper-arg-list"], "op"),         ")"]
properarglist               = ["proper-arg-list",           "arg",          Product(["sub-proper-arg-list"], "n")]
subproperarglist            = ["sub-proper-arg-list",       ",",            "arg"]
arg                         = ["arg",                       "expr"]

grammarTable = [program,
                funcdecl,
                vardecl,
                initdeclaratorlist,
                supinitdeclaratorlist,
                initdeclarator,
                supinitdeclarator,
                declarator,
                subdeclarator,
                initialiser,
                subinitialiser,
                subsubinitialiser,
                type,
                identifier, 
                compoundstmt,
                stmt,
                ifstmt,
                elsestmt,
                forstmt,
                whilestmt,
                breakstmt,
                continuestmt,
                returnstmt,
                exprstmt,
                expr,   
                assignmentexpr,
                subassignmentexpr,
                condorexpr,
                subcondorexpr,
                condandexpr,
                subcondandexpr,
                equalityexpr,
                equequalityexpr,
                nonequalityexpr,
                relexpr,
                lessrelexpr,
                lesserrelexpr,
                grwatrelexpr,
                greaterrelexpr,
                additiveexpr,
                addadditiveexpr,
                subadditiveexpr,
                multiplicativeexpr,
                mulmultiplicativeexpr,
                divmultiplicativeexpr,
                unaryexpr,
                plusunaryexpr,
                minusunaryexpr,
                reverseunaryexpr,
                primaryexpr,
                primaryexprtype,
                primaryexpr1,
                primaryexpr2,
                primaryexpr3,
                paralist,
                properparalist,
                subproperparalist,
                paradecl,
                arglist,
                properarglist,
                subproperarglist,
                arg]