# VC Grammar
```
semicolon       ";"
comma           ","
lbracket       "["
rbracket       "]"
equal           "="
lbraces        "{"
rbraces        "}"
lparentheses   "("
rparentheses   ")"
or              "||"
and             "&&"
equality        "=="
notequality    "!="
less            "<"
lesser          "<="
great           ">"
greater         ">="
plus            "+"
minus           "-"
mul             "*"
div             "/"
not             "!"
```

```xxx
PROGRAM                     -> PROGRAM PROGRAM
                             | TYPE DECL.
DECL                        -> FUNCDECL
                             | VARDECL .

FUNCDECL                    -> IDENTIFIER PARALIST COMPOUNDSTMT .

VARDECL                     -> INITDECLARATORLIST semicolon .

INITDECLARATORLIST          -> INITDECLARATOR comma INITDECLARATORLIST
                             | INITDECLARATOR .

INITDECLARATOR              -> DECLARATOR equal INITIALIZER
                             | DECLARATOR .

DECLARATOR                  -> IDENTIFIER 
                             | IDENTIFIER lbracket rbracket
                             | IDENTIFIER lbracket intliteral rbracket .

INITIALIZER                 -> EXPR
                             | lbraces EXPR rbraces
                             | lbraces EXPR SUBINITIALIZER rbraces .
SUBINITIALIZER              -> comma EXPR SUBINITIALIZER
                             | comma EXPR .

TYPE                        -> void
                             | boolean
                             | int
                             | float .

IDENTIFIER                  -> id .

COMPOUNDSTMT                -> lbraces VARDECLLIST STMTLIST rbraces .
VARDECLLIST                 -> VARDECLLIST VARDECLLIST
                             | VARDECL .
STMTLIST                    -> STMTLIST STMTLIST
                             | STMT .

STMT                        -> COMPOUNDSTMT
                             | IFSTMT
                             | FORSTMT
                             | WHILESTMT
                             | BREAKSTMT
                             | CONTINUESTMT
                             | RETURNSTMT
                             | EXPRSTMT .

IFSTMT                      -> if lparentheses EXPR rparentheses STMT
                             | if lparentheses EXPR rparentheses STMT else STMT .

FORSTMT                     -> for lparentheses FORSTMTEXPR semicolon FORSTMTEXPR semicolon FORSTMTEXPR rparentheses STMT .
MAYBEEXPR                   -> EXPR
                             | e .

WHILESTMT                   -> while lparentheses EXPR rparentheses STMT .

BREAKSTMT                   -> break semicolon .

CONTINUESTMT                -> continue semicolon .

RETURNSTMT                  -> return MAYBEEXPR semicolon .

EXPRSTMT                    -> MAYBEEXPR semicolon .

EXPR                        -> CONDOREXPR 
                             | EXPR equal CONDOREXPR .

CONDOREXPR                  -> CONDANDEXPR
                             | CONDOREXPR or CONDANDEXPR .

CONDANDEXPR                 -> EQUALITYEXPR
                             | CONDANDEXPR and EQUALITYEXPR .

EQUALITYEXPR                -> RELATIONALEXPR
                             | EQUALITYEXPR equality RELATIONALEXPR
                             | EQUALITYEXPR notequality RELATIONALEXPR .

RELATIONALEXPR              -> ADDITIVEEXPR
                             | RELATIONALEXPR less ADDITIVEEXPR
                             | RELATIONALEXPR lesser ADDITIVEEXPR
                             | RELATIONALEXPR great ADDITIVEEXPR
                             | RELATIONALEXPR greater ADDITIVEEXPR .

ADDITIVEEXPR                -> MULTIPLICATIVEEXPR
                             | ADDITIVEEXPR plus MULTIPLICATIVEEXPR
                             | ADDITIVEEXPR minus MULTIPLICATIVEEXPR .

MULTIPLICATIVEEXPR          -> UNARYEXPR
                             | MULTIPLICATIVEEXPR mul UNARYEXPR
                             | MULTIPLICATIVEEXPR div UNARYEXPR .

UNARYEXPR                   -> plus UNARYEXPR
                             | minus UNARYEXPR
                             | not UNARYEXPR
                             | PRIMARYEXPR .

PRIMARYEXPR                 -> IDENTIFIER
                             | IDENTIFIER ARGLIST
                             | IDENTIFIER lbracket EXPR rbracket
                             | lparentheses EXPR rparentheses
                             | intliteral
                             | floatliteral
                             | boolliteral
                             | stringliteral .

PARALIST                    -> lparentheses rparentheses
                             | lparentheses PROPERPARALIST rparentheses .

PROPERPARALIST              -> PARADECL comma PROPERPARALIST
                             | PARADECL .

PARADECL                    -> TYPE DECLARATOR .

ARGLIST                     -> lparentheses PROPERARGLIST rparentheses .

PROPERARGLIST               -> EXPR comma PROPERARGLIST
                             | EXPR .
```