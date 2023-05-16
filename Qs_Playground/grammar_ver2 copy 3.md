PROGRAM                         -> TYPE identifier SUBPROGRAM PROGRAM
PROGRAM                         -> ''
SUBPROGRAM                      -> FUNCDECL
SUBPROGRAM                      -> VARDECL 
FUNCDECL                        -> PARALIST COMPOUNDSTMT
VARDECL                         -> DECLARATOR INITDECLARATOR INITDECLARATORLIST semicolon
INITDECLARATORLIST              -> comma identifier DECLARATOR INITDECLARATOR INITDECLARATORLIST
INITDECLARATORLIST              -> ''
INITDECLARATOR                  -> equal INITIALISER
INITDECLARATOR                  -> ''
DECLARATOR                      -> lbracket SUBDECLARATOR
DECLARATOR                      -> ''
SUBDECLARATOR                   -> rbracket
SUBDECLARATOR                   -> intliteral rbracket
INITIALISER                     -> EXPR
INITIALISER                     -> lbrace EXPR SUBINITIALISER rbrace
SUBINITIALISER                  -> comma EXPR SUBINITIALISER
SUBINITIALISER                  -> ''
COMPOUNDSTMT                    -> lbrace SUBCOMPOUNDSTMT rbrace
SUBCOMPOUNDSTMT                 -> TYPE identifier VARDECL SUBCOMPOUNDSTMT
SUBCOMPOUNDSTMT                 -> STMT SUBCOMPOUNDSTMT
SUBCOMPOUNDSTMT                 -> ''
STMT                            -> IFSTMT
STMT                            -> FORSTMT
STMT                            -> WHILESTMT
STMT                            -> BREAKSTMT
STMT                            -> CONTINUESTMT
STMT                            -> RETURNSTMT
STMT                            -> EXPRSTMT
IFSTMT                          -> if lparent EXPR rparent COMPOUNDSTMT ELSESTMT
ELSESTMT                        -> else COMPOUNDSTMT
ELSESTMT                        -> ''
FORSTMT                         -> for lparent MAYBEEXPR semicolon MAYBEEXPR semicolon MAYBEEXPR rparent COMPOUNDSTMT
MAYBEEXPR                       -> EXPR
MAYBEEXPR                       -> ''
WHILESTMT                       -> while lparent EXPR rparent COMPOUNDSTMT
BREAKSTMT                       -> break semicolon
CONTINUESTMT                    -> continue semicolon
RETURNSTMT                      -> return MAYBEEXPR semicolon
EXPRSTMT                        -> EXPR semicolon
EXPRSTMT                        -> semicolon
EXPR                            -> ASSIGNMENTEXPR
ASSIGNMENTEXPR                  -> CONDOREXPR SUBASSIGNMENTEXPR 
SUBASSIGNMENTEXPR               -> equal CONDOREXPR SUBASSIGNMENTEXPR
SUBASSIGNMENTEXPR               -> ''
CONDOREXPR                      -> CONDANDEXPR SUBCONDOREXPR
SUBCONDOREXPR                   -> or CONDANDEXPR SUBCONDOREXPR
SUBCONDOREXPR                   -> ''
CONDANDEXPR                     -> EQUALITYEXPR SUBCONDANDEXPR 
SUBCONDANDEXPR                  -> and EQUALITYEXPR SUBCONDANDEXPR
SUBCONDANDEXPR                  -> ''
EQUALITYEXPR                    -> RELEXPR SUBEQUALITYEXPR
SUBEQUALITYEXPR                 -> equally RELEXPR SUBEQUALITYEXPR
SUBEQUALITYEXPR                 -> notequal RELEXPR SUBEQUALITYEXPR
SUBEQUALITYEXPR                 -> ''
RELEXPR                         -> ADDITIVEEXPR SUBRELEXPR
SUBRELEXPR                      -> less ADDITIVEEXPR SUBRELEXPR
SUBRELEXPR                      -> lesser ADDITIVEEXPR SUBRELEXPR
SUBRELEXPR                      -> great ADDITIVEEXPR SUBRELEXPR
SUBRELEXPR                      -> greater ADDITIVEEXPR SUBRELEXPR
SUBRELEXPR                      -> ''
ADDITIVEEXPR                    -> MULTIPLICATIVEEXPR SUBADDITIVEEXPR
SUBADDITIVEEXPR                 -> plus MULTIPLICATIVEEXPR SUBADDITIVEEXPR
SUBADDITIVEEXPR                 -> minus MULTIPLICATIVEEXPR SUBADDITIVEEXPR
SUBADDITIVEEXPR                 -> ''
MULTIPLICATIVEEXPR              -> UNARYEXPR SUBMULTIPLICATIVEEXPR
SUBMULTIPLICATIVEEXPR           -> mul UNARYEXPR SUBMULTIPLICATIVEEXPR
SUBMULTIPLICATIVEEXPR           -> slash UNARYEXPR SUBMULTIPLICATIVEEXPR
SUBMULTIPLICATIVEEXPR           -> ''
UNARYEXPR                       -> plus UNARYEXPR
UNARYEXPR                       -> minus UNARYEXPR
UNARYEXPR                       -> not UNARYEXPR
UNARYEXPR                       -> PRIMARYEXPR
PRIMARYEXPR                     -> identifier SUBPRIMARYEXPR
PRIMARYEXPR                     -> lparent EXPR rparent
PRIMARYEXPR                     -> intliteral
PRIMARYEXPR                     -> floatliteral
PRIMARYEXPR                     -> boolliteral
PRIMARYEXPR                     -> stringliteral
SUBPRIMARYEXPR                  -> ARGLIST
SUBPRIMARYEXPR                  -> lbracket EXPR rbracket
SUBPRIMARYEXPR                  -> ''
PARALIST                        -> lparent PROPERPARALIST rparent
PROPERPARALIST                  -> PARADECL SUBPROPERPARALIST
SUBPROPERPARALIST               -> comma PARADECL SUBPROPERPARALIST
SUBPROPERPARALIST               -> ''
PARADECL                        -> TYPE identifier DECLARATOR 
ARGLIST                         -> lparent PROPERARGLIST rparent
PROPERARGLIST                   -> ARG SUBPROPERARGLIST
PROPERARGLIST                   -> ''
SUBPROPERARGLIST                -> comma ARG SUBPROPERARGLIST
SUBPROPERARGLIST                -> ''
ARG                             -> EXPR 
TYPE                            -> void | int | float | boolean