grammar Expr;		

prog:	stat+ ;

stat:   expr NEWLINE
    |   ID '=' expr NEWLINE
    |   NEWLINE
    ;

expr:	expr ('*'|'/') expr
    |	expr ('+'|'-') expr
    |	INT
    |	'(' expr ')'
    ;
NEWLINE : '\r'? '\n' ;
ID      : [a-zA-Z] ;
INT     : [0-9]+ ;
WS      : [ \t]+ -> skip ;
