PROGRAM                     -> TYPE IDENTIFIER DECL PROGRAM
PROGRAM                     -> ''
DECL                        -> FUNCDECL
DECL                        -> VARDECL semicolon
FUNCDECL                    -> PARALIST COMPOUNDSTMT
VARDECL                     -> INITDECLARATOR INITDECLARATORLIST
INITDECLARATORLIST          -> , IDENTIFIER INITDECLARATOR INITDECLARATORLIST
INITDECLARATORLIST          -> ''
INITDECLARATOR              -> [ DECLARATOR ] SUBINITDECLARATOR
INITDECLARATOR              -> ''
SUBINITDECLARATOR           -> = INITIALIZER
SUBINITDECLARATOR           -> ''
DECLARATOR                  -> ''
DECLARATOR                  -> intliteral
INITIALIZER                 -> EXPR
INITIALIZER                 -> { EXPR SUBINITIALIZER }
SUBINITIALIZER              -> , EXPR SUBINITIALIZER
SUBINITIALIZER              -> ''
TYPE                        -> void
TYPE                        -> boolean
TYPE                        -> int
TYPE                        -> float
IDENTIFIER                  -> id
COMPOUNDSTMT                -> { SUBCOMPOUNDSTMT }
SUBCOMPOUNDSTMT             -> TYPE IDENTIFIER VARDECL SUBCOMPOUNDSTMT semicolon
SUBCOMPOUNDSTMT             -> STMT SUBCOMPOUNDSTMT semicolon
SUBCOMPOUNDSTMT             -> semicolon
STMT                        -> COMPOUNDSTMT
STMT                        -> IFSTMT
STMT                        -> FORSTMT
STMT                        -> WHILESTMT
STMT                        -> BREAKSTMT
STMT                        -> CONTINUESTMT
STMT                        -> RETURNSTMT
STMT                        -> EXPRSTMT
IFSTMT                      -> if ( EXPR ) STMT ELSESTMT
ELSESTMT                    -> else STMT
ELSESTMT                    -> ''
FORSTMT                     -> for ( MAYBEEXPR semicolon MAYBEEXPR semicolon MAYBEEXPR ) STMT
MAYBEEXPR                   -> EXPR
MAYBEEXPR                   -> ''
WHILESTMT                   -> while ( EXPR ) STMT
BREAKSTMT                   -> break semicolon
CONTINUESTMT                -> continue semicolon
RETURNSTMT                  -> return MAYBEEXPR semicolon
EXPRSTMT                    -> EXPR semicolon
EXPRSTMT                    -> semicolon
EXPR                        -> CONDOREXPR SUBEXPR
SUBEXPR                     -> = CONDOREXPR SUBEXPR
SUBEXPR                     -> ''
CONDOREXPR                  -> CONDANDEXPR SUBCONDOREXPR
SUBCONDOREXPR               -> || CONDANDEXPR SUBCONDOREXPR
SUBCONDOREXPR               -> ''
CONDANDEXPR                 -> EQUALITYEXPR SUBCONDANDEXPR
SUBCONDANDEXPR              -> && EQUALITYEXPR SUBCONDANDEXPR
SUBCONDANDEXPR              -> ''
EQUALITYEXPR                -> RELATIONALEXPR SUBEQUALITYEXPR
SUBEQUALITYEXPR             -> == RELATIONALEXPR SUBEQUALITYEXPR
SUBEQUALITYEXPR             -> != RELATIONALEXPR SUBEQUALITYEXPR
SUBEQUALITYEXPR             -> ''
RELATIONALEXPR              -> ADDITIVEEXPR SUBRELATIONALEXPR
SUBRELATIONALEXPR           -> < ADDITIVEEXPR SUBRELATIONALEXPR
SUBRELATIONALEXPR           -> <= ADDITIVEEXPR SUBRELATIONALEXPR
SUBRELATIONALEXPR           -> > ADDITIVEEXPR SUBRELATIONALEXPR
SUBRELATIONALEXPR           -> >= ADDITIVEEXPR SUBRELATIONALEXPR
SUBRELATIONALEXPR           -> ''
ADDITIVEEXPR                -> MULTIPLICATIVEEXPR SUBADDITIVEEXPR
SUBADDITIVEEXPR             -> + MULTIPLICATIVEEXPR SUBADDITIVEEXPR
SUBADDITIVEEXPR             -> - MULTIPLICATIVEEXPR SUBADDITIVEEXPR
SUBADDITIVEEXPR             -> ''
MULTIPLICATIVEEXPR          -> UNARYEXPR SUBMULTIPLICATIVEEXPR
SUBMULTIPLICATIVEEXPR       -> * UNARYEXPR SUBMULTIPLICATIVEEXPR
SUBMULTIPLICATIVEEXPR       -> / UNARYEXPR SUBMULTIPLICATIVEEXPR
SUBMULTIPLICATIVEEXPR       -> ''
UNARYEXPR                   -> + UNARYEXPR
UNARYEXPR                   -> - UNARYEXPR
UNARYEXPR                   -> ! UNARYEXPR
UNARYEXPR                   -> PRIMARYEXPR
PRIMARYEXPR                 -> IDENTIFIER SUBPRIMARYEXPR
PRIMARYEXPR                 -> ( EXPR )
PRIMARYEXPR                 -> intliteral
PRIMARYEXPR                 -> floatliteral
PRIMARYEXPR                 -> boolliteral
PRIMARYEXPR                 -> stringliteral
SUBPRIMARYEXPR              -> ''
SUBPRIMARYEXPR              -> ARGLIST
SUBPRIMARYEXPR              -> [ EXPR ]
PARALIST                    -> ( PROPERPARALIST )
PROPERPARALIST              -> PARADECL SUBPROPERPARALIST
PROPERPARALIST              -> ''
SUBPROPERPARALIST           -> , PARADECL SUBPROPERPARALIST
SUBPROPERPARALIST           -> ''
PARADECL                    -> TYPE IDENTIFIER SUBPARADECL
SUBPARADECL                 -> [ DECLARATOR ]
SUBPARADECL                 -> ''
ARGLIST                     -> ( PROPERARGLIST )
PROPERARGLIST               -> EXPR SUBPROPERARGLIST
PROPERARGLIST               -> ''
SUBPROPERARGLIST            -> , EXPR SUBPROPERARGLIST
SUBPROPERARGLIST            -> ''