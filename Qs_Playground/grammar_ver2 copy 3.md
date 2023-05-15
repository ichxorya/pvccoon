COMPOUNDSTMT                    -> lbrace SUPVARDECL SUBCOMPOUNDSTMT rbrace 
SUBCOMPOUNDSTMT                 -> SUPSTMT | ''
SUPVARDECL                      -> type identifier vardecl SUPVARDECL | ''
SUPSTMT                         -> STMT SUBSTMT 
SUBSTMT                         -> STMT SUBSTMT | ''
STMT                            -> COMPOUNDSTMT | IFSTMT | FORSTMT | WHILESTMT | BREAKSTMT | CONTINUESTMT | RETURNSTMT | EXPRSTMT 
IFSTMT                          -> if lparent expr rparent STMT ELSESTMT 
ELSESTMT                        -> else STMT | ''
FORSTMT                         -> for lparent MAYBEEXPR semicolon MAYBEEXPR semicolon MAYBEEXPR rparent STMT 
MAYBEEXPR                       -> expr | ''
WHILESTMT                       -> while lparent expr rparent STMT 
BREAKSTMT                       -> break semicolon 
CONTINUESTMT                    -> continue semicolon 
RETURNSTMT                      -> return MAYBEEXPR semicolon 
EXPRSTMT                        -> MAYBEEXPR semicolon

