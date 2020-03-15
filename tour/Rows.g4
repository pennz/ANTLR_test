grammar Rows;

@parser::members { // add members to generated RowsParser
    int col;
    public RowsParser(TokenStream input, int col) { // custom constructor
        this(input);
        this.col = col;
    }
}

file : (row NL)+ ; // NL is the newline tocken 
row
locals [int i=0]    // this goes to RowParser.row(), it returns RowContext
    : ( STUFF
        {
        $i++;
        if ( $i == col ) System.out.println(%STUFF.text); // print last column?
        }
    )+
    ;

TAB :   '\t' -> skip ;
NL  :   '\r'? '\n'  ;
STUFF:  ~[\t\r\n]+  ;


