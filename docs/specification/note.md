# Language Specification

-- 12:09, 14/02/2023.

Planned to reverse engineer this [.flex file](lamngcnguyen_vc.lex).
I wonder why there is no other usable Github project.

View the original file: <https://github.com/lamngcnguyen/vc_compiler/blob/master/src/main/jflex/vc.flex>

-- 13:28, 14/02/2023.
What ChatGPT told me:

```text
The lexer defined in the code snippet recognizes the following tokens:

Keywords: boolean, break, continue, else, for, float, if, int, return, void, while.
Operators: +, -, *, /, =, >, <, <=, >=, ==, !=, &&, ||, !, ++, --.
Separators: (, ), {, }, [, ], ;, ,.
Literals: integer literals, floating-point literals, string literals, boolean literals (true, false).
Comments: traditional comments (/* ... */), end-of-line comments (// ...), and documentation comments (/** ... */).
White spaces: line terminators (\r, \n, \r\n) and spaces, tabs, and form feeds.
Identifiers: any sequence of letters and digits that starts with a letter ([:jletter:] [:jletterdigit:]*).
```

Is this correct? Gotta check it out.
