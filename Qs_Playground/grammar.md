PROGRAM                     -> TYPE IDENTIFIER DECL PROGRAM | e .
DECL                        -> FUNCDECL | VARDECL .
FUNCDECL                    -> PARALIST COMPOUNDSTMT .
VARDECL                     -> INITDECLARATOR INITDECLARATORLIST semicolon .
INITDECLARATORLIST          -> comma IDENTIFIER INITDECLARATOR INITDECLARATORLIST | e .
INITDECLARATOR              -> lbracket DECLARATOR rbracket SUBINITDECLARATOR | e .
SUBINITDECLARATOR           -> equal INITIALIZER | e .
DECLARATOR                  -> intliteral | e .
INITIALIZER                 -> EXPR | lbraces EXPR SUBINITIALIZER rbraces .
SUBINITIALIZER              -> comma EXPR SUBINITIALIZER | e .
TYPE                        -> void | boolean | int | float .
IDENTIFIER                  -> id .
COMPOUNDSTMT                -> lbraces SUBCOMPOUNDSTMT rbraces .
SUBCOMPOUNDSTMT             -> TYPE IDENTIFIER VARDECL SUBCOMPOUNDSTMT | STMT SUBCOMPOUNDSTMT | e .
STMT                        -> COMPOUNDSTMT | IFSTMT | FORSTMT | WHILESTMT | BREAKSTMT | CONTINUESTMT | RETURNSTMT | EXPRSTMT .
IFSTMT                      -> if lparentheses EXPR rparentheses STMT ELSESTMT .
ELSESTMT                    -> else STMT | e .
FORSTMT                     -> for lparentheses MAYBEEXPR semicolon MAYBEEXPR semicolon MAYBEEXPR rparentheses STMT .
MAYBEEXPR                   -> EXPR | e .
WHILESTMT                   -> while lparentheses EXPR rparentheses STMT .
BREAKSTMT                   -> break semicolon .
CONTINUESTMT                -> continue semicolon .
RETURNSTMT                  -> return MAYBEEXPR semicolon .
EXPRSTMT                    -> EXPR semicolon  | semicolon.
EXPR                        -> CONDOREXPR SUBEXPR .
SUBEXPR                     -> equal CONDOREXPR SUBEXPR  | e .
CONDOREXPR                  -> CONDANDEXPR SUBCONDOREXPR .
SUBCONDOREXPR               -> or CONDANDEXPR SUBCONDOREXPR | e .
CONDANDEXPR                 -> EQUALITYEXPR SUBCONDANDEXPR .
SUBCONDANDEXPR              -> and EQUALITYEXPR SUBCONDANDEXPR | e .
EQUALITYEXPR                -> RELATIONALEXPR SUBEQUALITYEXPR .
SUBEQUALITYEXPR             -> equality RELATIONALEXPR SUBEQUALITYEXPR | notequality RELATIONALEXPR SUBEQUALITYEXPR | e .
RELATIONALEXPR              -> ADDITIVEEXPR SUBRELATIONALEXPR .
SUBRELATIONALEXPR           -> less ADDITIVEEXPR SUBRELATIONALEXPR | lesser ADDITIVEEXPR SUBRELATIONALEXPR | great ADDITIVEEXPR SUBRELATIONALEXPR | greater ADDITIVEEXPR SUBRELATIONALEXPR | e .
ADDITIVEEXPR                -> MULTIPLICATIVEEXPR SUBADDITIVEEXPR.
SUBADDITIVEEXPR             -> plus MULTIPLICATIVEEXPR SUBADDITIVEEXPR | minus MULTIPLICATIVEEXPR SUBADDITIVEEXPR  | e .
MULTIPLICATIVEEXPR          -> UNARYEXPR SUBMULTIPLICATIVEEXPR .
SUBMULTIPLICATIVEEXPR       -> mul UNARYEXPR SUBMULTIPLICATIVEEXPR | div UNARYEXPR SUBMULTIPLICATIVEEXPR  | e .
UNARYEXPR                   -> plus UNARYEXPR | minus UNARYEXPR | not UNARYEXPR | PRIMARYEXPR .
PRIMARYEXPR                 -> IDENTIFIER SUBPRIMARYEXPR | lparentheses EXPR rparentheses | intliteral | floatliteral | boolliteral | stringliteral .
SUBPRIMARYEXPR              -> e | ARGLIST | lbracket EXPR rbracket .
PARALIST                    -> lparentheses PROPERPARALIST rparentheses .                            
PROPERPARALIST              -> PARADECL SUBPROPERPARALIST | e .
SUBPROPERPARALIST           -> comma PARADECL SUBPROPERPARALIST | e .
PARADECL                    -> TYPE IDENTIFIER SUBPARADECL.
SUBPARADECL                 -> lbracket DECLARATOR rbracket | e .
ARGLIST                     -> lparentheses PROPERARGLIST rparentheses .
PROPERARGLIST               -> EXPR SUBPROPERARGLIST | e .
SUBPROPERARGLIST            -> comma EXPR SUBPROPERARGLIST | e .