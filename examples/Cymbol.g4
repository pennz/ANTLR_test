grammar Cymbol;

file: (functionDecl | varDecl | comment)+ ;
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
comment: '//' .*? NL;

ID  :   ALP (ALP | DIGIT)* ;
ALP :   [a-zA-Z] ;
DIGIT:  [0-9] ;

NL  : '\r'? '\n' ;
WS  : [ \t\n\r] -> skip ;
