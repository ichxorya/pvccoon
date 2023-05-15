PROGRAM                         -> FUNCDECL PROGRAM
                                 | VARDECL PROGRAM
                                 | .
FUNCDECL                        -> TYPE IDENTIFIER PARALIST COMPOUNDSTMT .
VARDECL                         -> TYPE INITDECLARATORLIST semicolon .
INITDECLARATORLIST              -> INITDECLARATOR SUBINITDECLARATORLIST .
SUBINITDECLARATORLIST           -> comma INITDECLARATOR SUBINITDECLARATORLIST
                                 | .
INITDECLARATOR                  -> DECLARATOR equal INITIALISER
                                 | DECLARATOR .
DECLARATOR                      -> IDENTIFIER
                                 | IDENTIFIER lbracket rbracket
                                 | IDENTIFIER lbracket intliteral rbracket .
INITIALISER                     -> EXPR
                                 | lbrace EXPR SUBINITIALISER rbrace .
SUBINITIALISER                  -> comma EXPR SUBINITIALISER
                                 | .
TYPE                            -> void
                                 | boolean
                                 | int
                                 | float .
IDENTIFIER                      -> id .
COMPOUNDSTMT                    -> lbrace SUPVARDECL SUPSTMT rbrace
                                 | lbrace SUPSTMT rbrace
                                 | lbrace rbrace .
SUPVARDECL                      -> VARDECL SUPVARDECL 
                                 | .
SUPSTMT                         -> STMT SUBSTMT .
SUBSTMT                         -> STMT SUBSTMT
                                 | .
STMT                            -> COMPOUNDSTMT
                                 | IFSTMT
                                 | FORSTMT
                                 | WHILESTMT
                                 | BREAKSTMT
                                 | CONTINUESTMT
                                 | RETURNSTMT
                                 | EXPRSTMT .
IFSTMT                          -> if lparent EXPR rparent STMT else STMT
                                 | if lparent EXPR rparent STMT .
FORSTMT                         -> for lparent MAYBEEXPR semicolon MAYBEEXPR semicolon MAYBEEXPR rparent STMT .
MAYBEEXPR                       -> EXPR
                                 |  .
WHILESTMT                       -> while lparent EXPR rparent STMT .
BREAKSTMT                       -> break semicolon .
CONTINUESTMT                    -> continue semicolon .
RETURNSTMT                      -> return MAYBEEXPR semicolon .
EXPRSTMT                        -> MAYBEEXPR semicolon .
EXPR                            -> ASSIGNMENTEXPR .
ASSIGNMENTEXPR                  -> SUBASSIGNMENTEXPR CONDOREXPR .
SUBASSIGNMENTEXPR               -> CONDOREXPR equal SUBASSIGNMENTEXPR
                                 |  .
CONDOREXPR                      -> CONDANDEXPR
                                 | CONDOREXPR or CONDANDEXPR .
CONDANDEXPR                     -> EQUALITYEXPR
                                 | CONDANDEXPR and EQUALITYEXPR .
EQUALITYEXPR                    -> RELEXPR
                                 | EQUALITYEXPR equally RELEXPR
                                 | EQUALITYEXPR notequal RELEXPR .
RELEXPR                         -> ADDITIVEEXPR
                                 | RELEXPR less ADDITIVEEXPR
                                 | RELEXPR lesser ADDITIVEEXPR
                                 | RELEXPR great ADDITIVEEXPR
                                 | RELEXPR greater ADDITIVEEXPR .
ADDITIVEEXPR                    -> MULTIPLICATIVEEXPR
                                 | ADDITIVEEXPR plus MULTIPLICATIVEEXPR
                                 | ADDITIVEEXPR minus MULTIPLICATIVEEXPR .
MULTIPLICATIVEEXPR              -> UNARYEXPR
                                 | MULTIPLICATIVEEXPR mul UNARYEXPR
                                 | MULTIPLICATIVEEXPR div UNARYEXPR .
UNARYEXPR                       -> plus UNARYEXPR
                                 | minus UNARYEXPR
                                 | not UNARYEXPR
                                 | PRIMARYEXPR .
PRIMARYEXPR                     -> IDENTIFIER
                                 | IDENTIFIER ARGLIST
                                 | IDENTIFIER lbracket EXPR rbracket
                                 | lparent EXPR rparent
                                 | intliteral
                                 | floatliteral
                                 | boolliteral
                                 | stringliteral .
PARALIST                        -> lparent PROPERPARALIST rparent .
PROPERPARALIST                  -> PARADECL SUBPROPERPARALIST .
SUBPROPERPARALIST               -> comma PARADECL SUBPROPERPARALIST
                                 | .
PARADECL                        -> TYPE DECLARATOR .
ARGLIST                         -> lparent PROPERARGLIST rparent .
PROPERARGLIST                   -> ARG SUBPROPERARGLIST 
                                 | .
SUBPROPERARGLIST                -> comma ARG SUBPROPERARGLIST
                                 | .
ARG                             -> EXPR .