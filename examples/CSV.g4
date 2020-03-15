grammar CSV;

file : row line* ; // maybe empty
row  : line ;
line : FIELD (',' FIELD)* '\r'? NL ;

FIELD 
    : TEXT
    | STRING
    |
    ;

TEXT : ~[,\n\r"]+ ;
STRING : '"' ('""'|~'"')* '"' ;
NL  : '\n' ;
WS  :   ' ' -> skip ;
