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

-- 8:32, 17/03/2023.

It's been a while since I last updated on this project. I'm going to start updating it again.
There was some problems (literally skill issues) with the first course project. The teaching assistant (Mr. Quan) did asked us to implement a table-driven lexer, and the automation should not be too... automatic. So, I don't think we could use any lexer-generator or such in this project. We have to do it on our own.

Two weeks before, I was speedrunning with the DFA, and yet we stopped at 80% then have to do it all over again because we misunderstood the language specification. Right now, the deadline is near (21/03/2023). We are going to try to finish it as soon as possible.

Also, I tried to implement a VSCode extension for this language. It's currently in the early stage, and can only highlight the keywords. I'm going to try to implement the lexer in the extension, so that it can highlight the tokens and do more stuff.

-- 9:57, 17/03/2023.

I'm planning to use the .csv format for the .dat file.
