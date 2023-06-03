parser grammar TemplateParser;
options { tokenVocab=TemplateLexer; }

template: ( TEMPLATE_TEXT
          | template_stmt
          | NOT_STMT
          )+ EOF ;


template_stmt : STMT_START stmt STMT_END ;

stmt: fn_call
    | json_ptr
    ;

expr: fn_call
    | json_ptr
    | rdf_class
    | num
    | str
    ;

fn_name: FN_NAME ;

fn_call: fn_name '(' expr (',' expr)* ')' ;

json_ptr: JSON_PTR ;

rdf_class: RDF_CLASS;

num: NUM ;

str_content: (ESC_CHAR | STR_CONTENT)* ;

str: STR_START str_content STR_END ;
