grammar Pred;

assign
    : ID '=' v=INT ';'
      {if ($v.int==0) System.out.println("values must be > 0");}
    ;
    //: ID '=' v=INT {$v.int>0}? ';'
    //  {System.out.println("assign "+$ID.text+" to ");}
    //; // this will force error for parser

INT :   [0-9]+ ;
ID  :   [a-zA-Z]+ ;
WS  :   [ \t\r\n]+ -> skip ;

