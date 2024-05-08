grammar dj;

// Lexer
fragment START_DIGIT: [1-9];
fragment DIGIT: [0-9];
fragment ZERO: '0';

INTEGER: (START_DIGIT DIGIT* | ZERO);
FLOAT: (INTEGER '.' DIGIT* START_DIGIT);
VALUE: INTEGER | FLOAT;

OPERATION: ('+' | '*' | '~' | '/');

LBR: '(';
RBR: ')';

COMMA: ',';

WS : [ \t\n\r]+ -> skip ;

// Parser
start: expression EOF; 

expression:
    OPERATION LBR operands RBR
    ;

operands:
    (value | expression) (COMMA (value | expression))*
    ;

value:
    INTEGER
    | FLOAT
    ;