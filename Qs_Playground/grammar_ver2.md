PROGRAM                         -> ( FUNCDECL | VARDECL )*
FUNCDECL                        -> TYPE IDENTIFIER PARALIST COMPOUNDSTMT
VARDECL                         -> TYPE INITDECLARATORLIST semicolon
INITDECLARATORLIST              -> INITDECLARATOR ( comma INITDECLARATOR )*
INITDECLARATOR                  -> DECLARATOR ( equal INITIALISER )?
DECLARATOR                      -> IDENTIFIER
                                 | IDENTIFIER lbracket intliteral? rbracket
INITIALISER                     -> EXPR
                                 | lbrace EXPR ( comma EXPR )* rbrace
TYPE                            -> void | boolean | int | float
IDENTIFIER                      -> ID
COMPOUNDSTMT                    -> lbrace VARDECL* STMT* rbrace
STMT                            -> COMPOUNDSTMT
                                 | IFSTMT
                                 | FORSTMT
                                 | WHILESTMT
                                 | BREAKSTMT|
                                 | CONTINUESTMT
                                 | RETURNSTMT
                                 | EXPRSTMT
IFSTMT                          -> if lparent EXPR rparent STMT ( else STMT )?
FORSTMT                         -> for lparent EXPR? semicolon EXPR? semicolon EXPR? rparent STMT
WHILESTMT                       -> while lparent EXPR rparent STMT
BREAKSTMT                       -> break semicolon
CONTINUESTMT                    -> continue semicolon
RETURNSTMT                      -> return EXPR? semicolon
EXPRSTMT                        -> EXPR? semicolon
EXPR                            -> ASSIGNMENTEXPR
ASSIGNMENTEXPR                  -> ( CONDOREXPR equal )* CONDOREXPR
CONDOREXPR                      -> CONDANDEXPR
                                 | CONDOREXPR or CONDANDEXPR
CONDANDEXPR                     -> EQUALITYEXPR
                                 | CONDANDEXPR and EQUALITYEXPR
EQUALITYEXPR                    -> RELEXPR
                                 | EQUALITYEXPR equally RELEXPR
                                 | EQUALITYEXPR notequal RELEXPR
RELEXPR                         -> ADDITIVEEXPR
                                 | RELEXPR less ADDITIVEEXPR
                                 | RELEXPR lesser ADDITIVEEXPR
                                 | RELEXPR great ADDITIVEEXPR
                                 | RELEXPR greater ADDITIVEEXPR
ADDITIVEEXPR                    -> MULTIPLICATIVEEXPR
                                 | ADDITIVEEXPR plus MULTIPLICATIVEEXPR
                                 | ADDITIVEEXPR minus MULTIPLICATIVEEXPR
MULTIPLICATIVEEXPR              -> UNARYEXPR
                                 | MULTIPLICATIVEEXPR mul UNARYEXPR
                                 | MULTIPLICATIVEEXPR div UNARYEXPR
UNARYEXPR                       -> plus UNARYEXPR
                                 | minus UNARYEXPR
                                 | not UNARYEXPR
                                 | PRIMARYEXPR
PRIMARYEXPR                     -> IDENTIFIER ARGLIST?
                                 | IDENTIFIER lbracket EXPR rbracket
                                 | lparent EXPR rparent
                                 | intliteral
                                 | floatliteral
                                 | boolliteral
                                 | stringliteral
PARALIST                        -> lparent PROPERPARALIST? rparent
PROPERPARALIST                  -> PARADECL ( comma PARADECL )*
PARADECL                        -> TYPE DECLARATOR
ARGLIST                         -> lparent PROPERARGLIST? rparent
PROPERARGLIST                   -> ARG ( comma ARG )*
ARG                             -> EXPR