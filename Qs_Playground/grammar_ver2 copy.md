PROGRAM                         -> type identifier SUBPROGRAM PROGRAM | ''
SUBPROGRAM                      -> FUNCDECL | VARDECL 
FUNCDECL                        -> PARALIST COMPOUNDSTMT
VARDECL                         -> DECLARATOR INITDECLARATOR INITDECLARATORLIST semicolon
INITDECLARATORLIST              -> comma identifier DECLARATOR INITDECLARATOR INITDECLARATORLIST | ''
INITDECLARATOR                  -> equal INITIALISER | ''
DECLARATOR                      -> lbracket SUBDECLARATOR | ''
SUBDECLARATOR                   -> rbracket | intliteral rbracket
INITIALISER                     -> EXPR | lbrace EXPR SUBINITIALISER rbrace
SUBINITIALISER                  -> comma EXPR SUBINITIALISER | ''
COMPOUNDSTMT                    -> lbrace SUPVARDECL SUBCOMPOUNDSTMT rbrace
SUBCOMPOUNDSTMT                 -> SUPSTMT | ''
SUPVARDECL                      -> type identifier VARDECL SUPVARDECL | ''
SUPSTMT                         -> STMT SUBSTMT
SUBSTMT                         -> STMT SUBSTMT | ''

STMT                            -> COMPOUNDSTMT | IFSTMT | FORSTMT | WHILESTMT | BREAKSTMT | CONTINUESTMT | RETURNSTMT | EXPRSTMT
IFSTMT                          -> if lparent EXPR rparent STMT ELSESTMT
ELSESTMT                        -> else STMT | ''
FORSTMT                         -> for lparent MAYBEEXPR semicolon MAYBEEXPR semicolon MAYBEEXPR rparent STMT
MAYBEEXPR                       -> EXPR | ''
WHILESTMT                       -> while lparent EXPR rparent STMT

BREAKSTMT                       -> break semicolon
CONTINUESTMT                    -> continue semicolon
RETURNSTMT                      -> return MAYBEEXPR semicolon
EXPRSTMT                        -> MAYBEEXPR semicolon
EXPR                            -> ASSIGNMENTEXPR
ASSIGNMENTEXPR                  -> CONDOREXPR SUBASSIGNMENTEXPR 
SUBASSIGNMENTEXPR               -> equal CONDOREXPR SUBASSIGNMENTEXPR | ''
CONDOREXPR                      -> CONDANDEXPR SUBCONDOREXPR
SUBCONDOREXPR                   -> or CONDANDEXPR SUBCONDOREXPR | ''
CONDANDEXPR                     -> EQUALITYEXPR SUBCONDANDEXPR 
SUBCONDANDEXPR                  -> and EQUALITYEXPR SUBCONDANDEXPR | ''
EQUALITYEXPR                    -> RELEXPR SUBEQUALITYEXPR
SUBEQUALITYEXPR                 -> equally RELEXPR SUBEQUALITYEXPR | notequal RELEXPR SUBEQUALITYEXPR | ''
RELEXPR                         -> ADDITIVEEXPR SUBRELEXPR
SUBRELEXPR                      -> less ADDITIVEEXPR SUBRELEXPR | lesser ADDITIVEEXPR SUBRELEXPR | great ADDITIVEEXPR SUBRELEXPR | greater ADDITIVEEXPR SUBRELEXPR | ''
ADDITIVEEXPR                    -> MULTIPLICATIVEEXPR SUBADDITIVEEXPR
SUBADDITIVEEXPR                 -> plus MULTIPLICATIVEEXPR SUBADDITIVEEXPR | minus MULTIPLICATIVEEXPR SUBADDITIVEEXPR | ''
MULTIPLICATIVEEXPR              -> UNARYEXPR SUBMULTIPLICATIVEEXPR
SUBMULTIPLICATIVEEXPR           -> mul UNARYEXPR SUBMULTIPLICATIVEEXPR | div UNARYEXPR SUBMULTIPLICATIVEEXPR | ''
UNARYEXPR                       -> plus UNARYEXPR | minus UNARYEXPR | not UNARYEXPR | PRIMARYEXPR
PRIMARYEXPR                     -> identifier SUBPRIMARYEXPR | lparent EXPR rparent | intliteral | floatliteral | boolliteral | stringliteral
SUBPRIMARYEXPR                  -> ARGLIST | lbracket EXPR rbracket | ''
PARALIST                        -> lparent PROPERPARALIST rparent
PROPERPARALIST                  -> PARADECL SUBPROPERPARALIST
SUBPROPERPARALIST               -> comma PARADECL SUBPROPERPARALIST | ''
PARADECL                        -> type identifier DECLARATOR 
ARGLIST                         -> lparent PROPERARGLIST rparent
PROPERARGLIST                   -> ARG SUBPROPERARGLIST | ''
SUBPROPERARGLIST                -> comma ARG SUBPROPERARGLIST | ''
ARG                             -> EXPR 