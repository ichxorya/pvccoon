PROGRAM                         -> TYPE identifier SUBPROGRAM PROGRAM | ''
SUBPROGRAM                      -> FUNCDECL | VARDECL 
FUNCDECL                        -> PARALIST COMPOUNDSTMT
VARDECL                         -> DECLARATOR SUBVARDECL
SUBVARDECL                      -> INITDECLARATOR SUBSUBSUBVARDECL | INITDECLARATORLIST semicolon | semicolon
SUBSUBSUBVARDECL                -> INITDECLARATORLIST semicolon | semicolon
INITDECLARATORLIST              -> comma identifier DECLARATOR INITDECLARATOR SUBINITDECLARATORLIST
SUBINITDECLARATORLIST           -> comma identifier DECLARATOR INITDECLARATOR SUBINITDECLARATORLIST | ''
INITDECLARATOR                  -> assign INITIALISER
DECLARATOR                      -> lbracket SUBDECLARATOR | ''
SUBDECLARATOR                   -> rbracket | intliteral rbracket
INITIALISER                     -> EXPR | lbrace EXPR SUBINITIALISER rbrace
SUBINITIALISER                  -> comma EXPR SUBINITIALISER | ''
COMPOUNDSTMT                    -> lbrace SUBCOMPOUNDSTMT rbrace
SUBCOMPOUNDSTMT                 -> SUBCOMPOUNDSTMT2 SUBCOMPOUNDSTMT | STMT SUBCOMPOUNDSTMT | ''
SUBCOMPOUNDSTMT2                -> TYPE identifier VARDECL
STMT                            -> IFSTMT | FORSTMT | WHILESTMT | BREAKSTMT | CONTINUESTMT | RETURNSTMT | EXPRSTMT
IFSTMT                          -> if lparen EXPR rparen COMPOUNDSTMT ELSESTMT
ELSESTMT                        -> else COMPOUNDSTMT | ''
FORSTMT                         -> for lparen MAYBEEXPR semicolon MAYBEEXPR semicolon MAYBEEXPR rparen COMPOUNDSTMT
MAYBEEXPR                       -> EXPR | ''
WHILESTMT                       -> while lparen EXPR rparen COMPOUNDSTMT
BREAKSTMT                       -> break semicolon
CONTINUESTMT                    -> continue semicolon
RETURNSTMT                      -> return MAYBEEXPR semicolon
EXPRSTMT                        -> EXPR semicolon | semicolon
EXPR                            -> ASSIGNMENTEXPR
ASSIGNMENTEXPR                  -> CONDOREXPR SUBASSIGNMENTEXPR 
SUBASSIGNMENTEXPR               -> assign CONDOREXPR SUBASSIGNMENTEXPR | ''
CONDOREXPR                      -> CONDANDEXPR SUBCONDOREXPR
SUBCONDOREXPR                   -> or CONDANDEXPR SUBCONDOREXPR | ''
CONDANDEXPR                     -> EQUALITYEXPR SUBCONDANDEXPR 
SUBCONDANDEXPR                  -> and EQUALITYEXPR SUBCONDANDEXPR | ''
EQUALITYEXPR                    -> RELEXPR SUBEQUALITYEXPR
SUBEQUALITYEXPR                 -> eq RELEXPR SUBEQUALITYEXPR | neq RELEXPR SUBEQUALITYEXPR | ''
RELEXPR                         -> ADDITIVEEXPR SUBRELEXPR
SUBRELEXPR                      -> lt ADDITIVEEXPR SUBRELEXPR | lte ADDITIVEEXPR SUBRELEXPR | gt ADDITIVEEXPR SUBRELEXPR | gte ADDITIVEEXPR SUBRELEXPR | ''
ADDITIVEEXPR                    -> MULTIPLICATIVEEXPR SUBADDITIVEEXPR
SUBADDITIVEEXPR                 -> plus MULTIPLICATIVEEXPR SUBADDITIVEEXPR | minus MULTIPLICATIVEEXPR SUBADDITIVEEXPR | ''
MULTIPLICATIVEEXPR              -> UNARYEXPR SUBMULTIPLICATIVEEXPR
SUBMULTIPLICATIVEEXPR           -> star UNARYEXPR SUBMULTIPLICATIVEEXPR | slash UNARYEXPR SUBMULTIPLICATIVEEXPR | ''
UNARYEXPR                       -> plus UNARYEXPR | minus UNARYEXPR | not UNARYEXPR | PRIMARYEXPR
PRIMARYEXPR                     -> identifier SUBPRIMARYEXPR | lparen EXPR rparen | intliteral | floatliteral | boolliteral | stringliteral
SUBPRIMARYEXPR                  -> ARGLIST | lbracket EXPR rbracket | ''
PARALIST                        -> lparen PROPERPARALIST rparen
PROPERPARALIST                  -> PARADECL SUBPROPERPARALIST | ''
SUBPROPERPARALIST               -> comma PARADECL SUBPROPERPARALIST | ''
PARADECL                        -> TYPE identifier DECLARATOR 
ARGLIST                         -> lparen PROPERARGLIST rparen
PROPERARGLIST                   -> ARG SUBPROPERARGLIST | ''
SUBPROPERARGLIST                -> comma ARG SUBPROPERARGLIST | ''
ARG                             -> EXPR 
TYPE                            -> boolean | int | void | float