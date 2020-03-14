grammar LibExpr; // Rename to distinguish from original
import CommonLexerRules; // includes all rules from CommonLexerRules.g4 

/** The start rule; begin parsing here. */
prog: stat+ ;

stat: expr NEWLINE          # printExpr
    | ID '=' expr NEWLINE   # assign
    | NEWLINE               # blank
    ;

expr: expr ('*'|'/') expr   # MulDiv
    | expr ('+'|'-') expr   # AddSub
    | INT                   # int
    | ID                    # id
    | '(' expr ')'          # parens
    ;
