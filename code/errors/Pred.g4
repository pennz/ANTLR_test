grammar Pred;

assign
    : ID '=' v=INT ';'
      {if ($v.int==0) System.out.println("values must be > 0");}
    ;

INT :   [0-9]+ ;
ID  :   [a-zA-Z]+ ;
WS  :   [ \t\r\n]+ -> skip ;

