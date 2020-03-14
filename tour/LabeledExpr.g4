grammar LabeledExpr; // Rename to distinguish from original
import CommonLexerRules; // includes all rules from CommonLexerRules.g4 

/** The start rule; begin parsing here. */
prog: stat+ ;

stat: expr NEWLINE          # printExpr
    | ID '=' expr NEWLINE   # assign
    | NEWLINE               # blank
    | CLEAR                 # clear
    ;

expr: expr op=('*'|'/') expr   # MulDiv
    | expr op=('+'|'-') expr   # AddSub
    | INT                   # int
    | ID                    # id
    | '(' expr ')'          # parens
    ;

MUL : '*' ; // assigns token name to '*' used above in grammar 
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
CLEAR: 'clear' ;
