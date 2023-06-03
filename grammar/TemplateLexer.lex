lexer grammar TemplateLexer;

TEMPLATE_TEXT : ~[<]+ ;
STMT_START : '<<' -> pushMode(STMT_MODE) ;
NOT_STMT : '<' ;

mode STMT_MODE;
    STMT_END : '>>' -> popMode ;

    COMMA : ',' ;
    SEMI : ';' ;
    COLON : ':' ;
    LPAREN : '(' ;
    RPAREN : ')' ;
    LCURLY : '{' ;
    RCURLY : '}' ;
    SLASH : '/' ;
    PERIOD : '.' ;
    DASH : '-' ;

    fragment QUOTE : '\'' ;
    fragment BACKSLASH : '\\';
    fragment ALPHA : [a-zA-Z] ;
    fragment DIGIT : [0-9] ;
    fragment ID_SYMBOLS : [_.-] ;
    fragment ALPHA_NUMERIC : ALPHA|DIGIT;

    NUM: '-'? DIGIT+ ('.' DIGIT+)? ([eE] [-+]? DIGIT+)? ;

    FN_NAME : ALPHA (ALPHA_NUMERIC | '_')* ;

    ID: (ALPHA_NUMERIC | ID_SYMBOLS)+ ;

    JSON_PTR: '/' ID ('/' ID)* ;

    RDF_CLASS: ID ':' ID ;

    WS : [ \t\n\r\f]+ -> skip ;

    STR_START : QUOTE -> pushMode(STR_MODE) ;

mode STR_MODE;
    STR_END : QUOTE -> popMode ;
    ESC : BACKSLASH -> skip, pushMode(STR_ESC_MODE) ;
    STR_CONTENT : ~['\\]+ ;

mode STR_ESC_MODE;
    ESC_CHAR :
             ( QUOTE
             | BACKSLASH
             ) -> popMode ;
