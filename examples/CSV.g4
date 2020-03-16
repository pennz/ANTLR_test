grammar CSV;

file : hdr row* ; // maybe empty
hdr  : row ;
row : FIELD (',' FIELD)* '\r'? NL ;

FIELD
    : TEXT
    | STRING
    |
    ;

TEXT : ~[,\n\r"]+ ;
STRING : '"' ('""'|~'"')* '"' ;
NL  : '\n' ;
WS  :   ' ' -> skip ;
