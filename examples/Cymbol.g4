grammar Cymbol;

file: (functionDecl | varDecl) + ;
varDecl
    : type ID ( '=' expr)? ';'
    ;
type: 'float' | 'int' | 'void' ;
functionDecl
    : type ID '(' formalParameters? ')' block
    ;
formalParameters
    : formalParameter (',' formalParameter)*
    ;
formalParameter
    : type ID
    ;
block: '{' stat* '}' ;
stat:   block
    |   varDecl
    |   'if' expr 'then' stat ('else' stat)?
    |   'return' expr? ';'
    |   expr '=' expr ';'
    |   expr ';'
    ;
expr:   ID '(' exprList? ')'
    |   expr '[' expr ']'
    |   '-' expr    // unary minus
    |   '!' expr    // boolean not
    |   expr '*' expr
    |   expr ('+'|'-') expr
    |   expr '==' expr
    |   ID                  // variable reference
    |   INT
    |   '(' expr ')'
    ;
exprList:   expr (',' expr)* ;
// comment: '//' .*? NL; // just ignore it in the lexer

ID  :   ALP (ALP | DIGIT)* ;
fragment
ALP :   [a-zA-Z] ;
fragment
DIGIT:  [0-9] ;
INT :   DIGIT+ ;

// NL  : '\r'? '\n' ;
WS  : [ \t\n\r]+ -> skip ;

SL_COMMENT: '//' .*? '\n' -> skip ; // just ignore it in the lexer
