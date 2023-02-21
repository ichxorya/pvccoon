import java_cup.runtime.*; 
%%

%public
%class VCScanner
%implements sym

%unicode
%line
%column

%cup
%cupdebug

%{
    StringBuilder stringBuilder = new StringBuilder();
    private Symbol symbol(int type) {
        return new VcSymbol(type, yyline+1, yycolumn+1);
    }
    private Symbol symbol(int type, Object value) {
        return new VcSymbol(type, yyline+1, yycolumn+1, value);
    }
%}

/* Defenitions */
LineTerminator = \r|\n|\r\n
InputCharacter = [^\r\n]
Whitespace = {LineTerminator} | [ \t\f]

/* Comments */
Comment = {TraditionalComment} | {EndOfLineComment} | {DocumentationComment}

TraditionalComment   = "/*" [^*] ~"*/" | "/*" "*"+ "/"
// Comment can be the last line of the file, without line terminator.
EndOfLineComment     = "//" {InputCharacter}* {LineTerminator}?
DocumentationComment = "/**" {CommentContent} "*"+ "/"
CommentContent       = ( [^*] | \*+ [^/*] )*

Identifier = [:jletter:] [:jletterdigit:]*

IntegerLiteral = 0 | [1-9][0-9]*

/* floating point literals */
FloatLiteral  = ({FLit1}|{FLit2}|{FLit3}) {Exponent}?

FLit1    = [0-9]+\.[0-9]*
FLit2    = \.[0-9]+
FLit3    = [0-9]+
Exponent = [eE][+-]?[0-9]+

/* string and character literals */
StringCharacter = [^\r\n\"\\]

%state STRING

%%
<YYINITIAL> {
    /* keywords */
    "boolean"   {return symbol(BOOLEAN);}
    "break"     {return symbol(BREAK);}
    "continue"  {return symbol(CONTINUE);}
    "else"      {return symbol(ELSE);}
    "for"       {return symbol(FOR);}
    "float"     {return symbol(FLOAT);}
    "if"        {return symbol(IF);}
    "int"       {return symbol(INT);}
    "return"    {return symbol(RETURN);}
    "void"      {return symbol(VOID);}
    "while"     {return symbol(WHILE);}

    /* operators */
    "+"         {return symbol(PLUS);}
    "-"         {return symbol(MINUS);}
    "*"         {return symbol(MULT);}
    "/"         {return symbol(DIV);}
    "="         {return symbol(EQ);}
    ">"         {return symbol(GT);}
    "<"         {return symbol(LT);}
    "<="        {return symbol(LTEQ);}
    ">="        {return symbol(GTEQ);}
    "=="        {return symbol(EQEQ);}
    "!="        {return symbol(NOTEQ);}
    "&&"        {return symbol(ANDAND);}
    "||"        {return symbol(OROR);}
    "!"         {return symbol(NOT);}
    "++"        {return symbol(PLUSPLUS);}
    "--"        {return symbol(MINUSMINUS);}

    /* separators */
    "("         {return symbol(LPAREN);}
    ")"         {return symbol(RPAREN);}
    "{"         {return symbol(LBRACE);}
    "}"         {return symbol(RBRACE);}
    "["         {return symbol(LBRACK);}
    "]"         {return symbol(RBRACK);}
    ";"         {return symbol(SEMICOLON);}
    ","         {return symbol(COMMA);}

    "true"      {return symbol(BOOLEAN_LITERAL, true);}
    "false"     {return symbol(BOOLEAN_LITERAL, false);}

    {Comment}       {/* ignored */}
    {Whitespace}    {/* ignored */}

    {Identifier}        {return symbol(IDENTIFIER, yytext());}
    {IntegerLiteral}    {return symbol(INTEGER_LITERAL, Integer.valueOf(yytext()));}
    {FloatLiteral}      {return symbol(FLOATING_POINT_LITERAL, new Float(yytext()));}
    \"                  {yybegin(STRING); stringBuilder.setLength(0);} //String literal
}

<STRING> {
    \"                      {yybegin(YYINITIAL); return symbol(STRING_LITERAL, stringBuilder.toString());}
    {StringCharacter}+      {stringBuilder.append(yytext());}
    "\\b"                   {stringBuilder.append('\b');}
    "\\t"                   {stringBuilder.append('\t');}
    "\\n"                   {stringBuilder.append('\n');}
    "\\f"                   {stringBuilder.append('\f');}
    "\\r"                   {stringBuilder.append('\r');}
    "\\\""                  {stringBuilder.append('\"');}
    "\\'"                   {stringBuilder.append('\'');}
    "\\\\"                  {stringBuilder.append('\\');}
}

[^]             {throw new RuntimeException("Illegal character: " + yytext() + " at line " + (yyline+1) + ", column " + (yycolumn+1));}
<<EOF>>         {return symbol(EOF);}