parser grammar TemplateParser;
options { tokenVocab=TemplateLexer; }

root: template EOF ;

template: ( TEMPLATE_TEXT
          | template_stmt
          | cond_template
          | NOT_STMT
          )+ ;

cond_template: STMT_START cond_start STMT_END
               template
               STMT_START cond_end STMT_END
             ;

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

cond_start : COND_START cond_list ;

cond_end : COND_END ;

cond_list : JSON_PTR ('&' JSON_PTR)* ;

fn_name: FN_NAME ;

fn_call: fn_name '(' expr (',' expr)* ')' ;

json_ptr: JSON_PTR ;

rdf_class: RDF_CLASS;

num: NUM ;

str_content: (ESC_CHAR | STR_CONTENT)* ;

str: STR_START str_content STR_END ;
