use logos::Logos;

#[derive(Logos, Debug, PartialEq)]
enum Token {
    // Keywords: boolean, break, continue, else, for, float, if, int, return, void, while.
    #[token("boolean")]
    Boolean,

    #[token("break")]
    Break,

    #[token("continue")]
    Continue,

    #[token("else")]
    Else,

    #[token("for")]
    For,

    #[token("float")]
    Float,

    #[token("if")]
    If,

    #[token("int")]
    Int,

    #[token("return")]
    Return,

    #[token("void")]
    Void,

    #[token("while")]
    While,

    // Operators: +, -, *, /, =, >, <, <=, >=, ==, !=, &&, ||, !, ++, --.
    #[token("+")]
    Plus,

    #[token("-")]
    Minus,

    #[token("*")]
    Star,

    #[token("/")]
    Slash,

    #[token("=")]
    Equal,

    #[token(">")]
    Greater,

    #[token("<")]
    Less,

    #[token("<=")]
    LessEqual,

    #[token(">=")]
    GreaterEqual,

    #[token("==")]
    EqualEqual,

    #[token("!=")]
    NotEqual,

    #[token("&&")]
    And,

    #[token("||")]
    Or,

    #[token("!")]
    Not,

    #[token("++")]
    Increment,

    #[token("--")]
    Decrement,

    // Separators: (, ), {, }, [, ], ;, ,.
    #[token("(")]
    LeftParen,

    #[token(")")]
    RightParen,

    #[token("{")]
    LeftBrace,

    #[token("}")]
    RightBrace,

    #[token("[")]
    LeftBracket,

    #[token("]")]
    RightBracket,

    #[token(";")]
    Semicolon,

    #[token(",")]
    Comma,

    // Literals: integer literals, floating-point literals, 
    //           string literals, boolean literals (true, false).
    #[regex(r"[0-9]+")]
    IntLiteral,

    #[regex(r"[0-9]+\.[0-9]+")] 
    FloatLiteral,

    #[regex(r#""[^"]*""#)]
    StringLiteral,

    #[token("true")]
    TrueBooleanLiteral,

    #[token("false")]
    FalseBooleanLiteral,

    // Comments: multi-line comments (/* ... */), single-line comments (// ...), 
    //           and documentation comments (/** ... */).
    #[regex(r"/\*.*\*/", logos::skip)]
    MultiLineComment,

    #[regex(r"/\*\*.*\*/", logos::skip)]
    DocumentationComment,

    #[regex(r"//.*", logos::skip)]
    SingleLineComment,

    // White spaces: line terminators (\r, \n, \r\n) and spaces, tabs, and form feeds.
    #[regex(r"[ \t\f]+", logos::skip)]
    WhiteSpace,

    #[regex(r"[\r\n]+", logos::skip)]
    LineTerminator,

    // Identifiers: any sequence of letters and digits that starts with a letter.
    #[regex(r"[a-zA-Z_][a-zA-Z0-9_]*")]
    Identifier,

    // Error.
    #[error]
    Error,
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_tokenizer() {
        let mut lex = Token::lexer("int ligma = 69;\n\nint ligma2 = 420;");
        while let Some(token) = lex.next() {
            println!("{:?}", token);
        }
    }
}