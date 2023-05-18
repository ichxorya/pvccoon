# Converted grammar of the VC Language

PROGRAM                         -> TYPE identifier SUBPROGRAM PROGRAM | ε
SUBPROGRAM                      -> FUNCDECL | VARDECL
FUNCDECL                        -> PARALIST COMPOUNDSTMT
VARDECL                         -> DECLARATOR SUBVARDECL
SUBVARDECL                      -> INITDECLARATOR SUBSUBSUBVARDECL | INITDECLARATORLIST semicolon | semicolon
SUBSUBSUBVARDECL                -> INITDECLARATORLIST semicolon | semicolon
INITDECLARATORLIST              -> comma identifier DECLARATOR INITDECLARATOR SUBINITDECLARATORLIST
SUBINITDECLARATORLIST           -> comma identifier DECLARATOR INITDECLARATOR SUBINITDECLARATORLIST | ε
INITDECLARATOR                  -> assign INITIALISER
DECLARATOR                      -> lbracket SUBDECLARATOR | ε
SUBDECLARATOR                   -> rbracket | intliteral rbracket
INITIALISER                     -> EXPR | lbrace EXPR SUBINITIALISER rbrace
SUBINITIALISER                  -> comma EXPR SUBINITIALISER | ε
COMPOUNDSTMT                    -> lbrace SUBCOMPOUNDSTMT rbrace
SUBCOMPOUNDSTMT                 -> SUBCOMPOUNDSTMT2 SUBCOMPOUNDSTMT | STMT SUBCOMPOUNDSTMT | ε
SUBCOMPOUNDSTMT2                -> TYPE identifier VARDECL
STMT                            -> IFSTMT | FORSTMT | WHILESTMT | BREAKSTMT | CONTINUESTMT | RETURNSTMT | EXPRSTMT
IFSTMT                          -> if lparen EXPR rparen COMPOUNDSTMT ELSESTMT
ELSESTMT                        -> else COMPOUNDSTMT | ε
FORSTMT                         -> for lparen MAYBEEXPR semicolon MAYBEEXPR semicolon MAYBEEXPR rparen COMPOUNDSTMT
MAYBEEXPR                       -> EXPR | ε
WHILESTMT                       -> while lparen EXPR rparen COMPOUNDSTMT
BREAKSTMT                       -> break semicolon
CONTINUESTMT                    -> continue semicolon
RETURNSTMT                      -> return MAYBEEXPR semicolon
EXPRSTMT                        -> EXPR semicolon | semicolon
EXPR                            -> ASSIGNMENTEXPR
ASSIGNMENTEXPR                  -> CONDOREXPR SUBASSIGNMENTEXPR
SUBASSIGNMENTEXPR               -> assign CONDOREXPR SUBASSIGNMENTEXPR | ε
CONDOREXPR                      -> CONDANDEXPR SUBCONDOREXPR
SUBCONDOREXPR                   -> or CONDANDEXPR SUBCONDOREXPR | ε
CONDANDEXPR                     -> EQUALITYEXPR SUBCONDANDEXPR
SUBCONDANDEXPR                  -> and EQUALITYEXPR SUBCONDANDEXPR | ε
EQUALITYEXPR                    -> RELEXPR SUBEQUALITYEXPR
SUBEQUALITYEXPR                 -> eq RELEXPR SUBEQUALITYEXPR | neq RELEXPR SUBEQUALITYEXPR | ε
RELEXPR                         -> ADDITIVEEXPR SUBRELEXPR
SUBRELEXPR                      -> lt ADDITIVEEXPR SUBRELEXPR | lte ADDITIVEEXPR SUBRELEXPR | gt ADDITIVEEXPR SUBRELEXPR | gte ADDITIVEEXPR SUBRELEXPR | ε
ADDITIVEEXPR                    -> MULTIPLICATIVEEXPR SUBADDITIVEEXPR
SUBADDITIVEEXPR                 -> plus MULTIPLICATIVEEXPR SUBADDITIVEEXPR | minus MULTIPLICATIVEEXPR SUBADDITIVEEXPR | ε
MULTIPLICATIVEEXPR              -> UNARYEXPR SUBMULTIPLICATIVEEXPR
SUBMULTIPLICATIVEEXPR           -> star UNARYEXPR SUBMULTIPLICATIVEEXPR | slash UNARYEXPR SUBMULTIPLICATIVEEXPR | ε
UNARYEXPR                       -> plus UNARYEXPR | minus UNARYEXPR | not UNARYEXPR | PRIMARYEXPR
PRIMARYEXPR                     -> identifier SUBPRIMARYEXPR | lparen EXPR rparen | intliteral | floatliteral | boolliteral | stringliteral
SUBPRIMARYEXPR                  -> ARGLIST | lbracket EXPR rbracket | ε
PARALIST                        -> lparen PROPERPARALIST rparen
PROPERPARALIST                  -> PARADECL SUBPROPERPARALIST | ε
SUBPROPERPARALIST               -> comma PARADECL SUBPROPERPARALIST | ε
PARADECL                        -> TYPE identifier DECLARATOR
ARGLIST                         -> lparen PROPERARGLIST rparen
PROPERARGLIST                   -> ARG SUBPROPERARGLIST | ε
SUBPROPERARGLIST                -> comma ARG SUBPROPERARGLIST | ε
ARG                             -> EXPR
TYPE                            -> boolean | int | void | float
