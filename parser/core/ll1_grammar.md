# Converted grammar of the VC Language

PROGRAM                         -> TYPE identifier SUBPROGRAM PROGRAM | epsilon
SUBPROGRAM                      -> FUNCDECL | VARDECL
FUNCDECL                        -> PARALIST COMPOUNDSTMT
VARDECL                         -> DECLARATOR SUBVARDECL
SUBVARDECL                      -> INITDECLARATOR SUBSUBSUBVARDECL | INITDECLARATORLIST semicolon | semicolon
SUBSUBSUBVARDECL                -> INITDECLARATORLIST semicolon | semicolon
INITDECLARATORLIST              -> comma identifier DECLARATOR INITDECLARATOR SUBINITDECLARATORLIST
SUBINITDECLARATORLIST           -> comma identifier DECLARATOR INITDECLARATOR SUBINITDECLARATORLIST | epsilon
INITDECLARATOR                  -> assign INITIALISER
DECLARATOR                      -> lbracket SUBDECLARATOR | epsilon
SUBDECLARATOR                   -> rbracket | intliteral rbracket
INITIALISER                     -> EXPR | lbrace EXPR SUBINITIALISER rbrace
SUBINITIALISER                  -> comma EXPR SUBINITIALISER | epsilon
COMPOUNDSTMT                    -> lbrace SUBCOMPOUNDSTMT rbrace
SUBCOMPOUNDSTMT                 -> SUBCOMPOUNDSTMT2 SUBCOMPOUNDSTMT | STMT SUBCOMPOUNDSTMT | epsilon
SUBCOMPOUNDSTMT2                -> TYPE identifier VARDECL
STMT                            -> IFSTMT | FORSTMT | WHILESTMT | BREAKSTMT | CONTINUESTMT | RETURNSTMT | EXPRSTMT
IFSTMT                          -> if lparen EXPR rparen COMPOUNDSTMT ELSESTMT
ELSESTMT                        -> else COMPOUNDSTMT | epsilon
FORSTMT                         -> for lparen MAYBEEXPR semicolon MAYBEEXPR semicolon MAYBEEXPR rparen COMPOUNDSTMT
MAYBEEXPR                       -> EXPR | epsilon
WHILESTMT                       -> while lparen EXPR rparen COMPOUNDSTMT
BREAKSTMT                       -> break semicolon
CONTINUESTMT                    -> continue semicolon
RETURNSTMT                      -> return MAYBEEXPR semicolon
EXPRSTMT                        -> EXPR semicolon | semicolon
EXPR                            -> ASSIGNMENTEXPR
ASSIGNMENTEXPR                  -> CONDOREXPR SUBASSIGNMENTEXPR
SUBASSIGNMENTEXPR               -> assign CONDOREXPR SUBASSIGNMENTEXPR | epsilon
CONDOREXPR                      -> CONDANDEXPR SUBCONDOREXPR
SUBCONDOREXPR                   -> or CONDANDEXPR SUBCONDOREXPR | epsilon
CONDANDEXPR                     -> EQUALITYEXPR SUBCONDANDEXPR
SUBCONDANDEXPR                  -> and EQUALITYEXPR SUBCONDANDEXPR | epsilon
EQUALITYEXPR                    -> RELEXPR SUBEQUALITYEXPR
SUBEQUALITYEXPR                 -> eq RELEXPR SUBEQUALITYEXPR | neq RELEXPR SUBEQUALITYEXPR | epsilon
RELEXPR                         -> ADDITIVEEXPR SUBRELEXPR
SUBRELEXPR                      -> lt ADDITIVEEXPR SUBRELEXPR | lte ADDITIVEEXPR SUBRELEXPR | gt ADDITIVEEXPR SUBRELEXPR | gte ADDITIVEEXPR SUBRELEXPR | epsilon
ADDITIVEEXPR                    -> MULTIPLICATIVEEXPR SUBADDITIVEEXPR
SUBADDITIVEEXPR                 -> plus MULTIPLICATIVEEXPR SUBADDITIVEEXPR | minus MULTIPLICATIVEEXPR SUBADDITIVEEXPR | epsilon
MULTIPLICATIVEEXPR              -> UNARYEXPR SUBMULTIPLICATIVEEXPR
SUBMULTIPLICATIVEEXPR           -> star UNARYEXPR SUBMULTIPLICATIVEEXPR | slash UNARYEXPR SUBMULTIPLICATIVEEXPR | epsilon
UNARYEXPR                       -> plus UNARYEXPR | minus UNARYEXPR | not UNARYEXPR | PRIMARYEXPR
PRIMARYEXPR                     -> identifier SUBPRIMARYEXPR | lparen EXPR rparen | intliteral | floatliteral | boolliteral | stringliteral
SUBPRIMARYEXPR                  -> ARGLIST | lbracket EXPR rbracket | epsilon
PARALIST                        -> lparen PROPERPARALIST rparen
PROPERPARALIST                  -> PARADECL SUBPROPERPARALIST | epsilon
SUBPROPERPARALIST               -> comma PARADECL SUBPROPERPARALIST | epsilon
PARADECL                        -> TYPE identifier DECLARATOR
ARGLIST                         -> lparen PROPERARGLIST rparen
PROPERARGLIST                   -> ARG SUBPROPERARGLIST | epsilon
SUBPROPERARGLIST                -> comma ARG SUBPROPERARGLIST | epsilon
ARG                             -> EXPR
TYPE                            -> boolean | int | void | float
