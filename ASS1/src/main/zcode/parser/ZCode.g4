grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: stmt+ EOF;

// Statements
stmt: (vardecl
	| im_vardecl
	| im_dydecl
	| funcdecl
	| builtin
	| funccall
	| arraydecl
	| assignstmt
	| ifstmt
	| forstmt
	| otherstmt
	| expr) NEWLINE*?;

	// Declarations
		// Variable declaration
vardecl: typ (IDENTIFIER | expr7) (ARROW expr)? ; // expr7 is for IDENTIFIER + index operator, which is an array element, for example : a[5]
im_vardecl: VAR IDENTIFIER ARROW expr ;
im_dydecl: DYNAMIC IDENTIFIER (ARROW expr)? ;

		// Function declaration
funcdecl: FUNC func funcend?;
func: IDENTIFIER arg ;
arg: LPAREN arglist RPAREN;
arglist: argprime | ;
argprime: argment COMMA argprime | argment;
argment: typ expr ;
funcend: returnstmt | blockstmt ;

		// Built-in function
builtin: readnum | writenum |readbool | writebool | readstr | writestr;
readnum: 'readNumber()' ;
writenum: 'writeNumber(' expr ')' ;
readbool: 'readBool()' ;
writebool: 'writeBool(' expr ')' ;
readstr: 'readString()' ;
writestr: 'writeString(' expr ')' ;

		// Array declaration
arraydecl: typ IDENTIFIER LBRACKET arraydim RBRACKET ARROW array ;
arraydim: NUMBER_LITERAL COMMA arraydim | NUMBER_LITERAL;
array: LBRACKET arraylist RBRACKET ;
arraylist: arrayobj | ;
arrayobj: arrayelement COMMA arrayobj | arrayelement ;
arrayelement: literals | array;

	// Assignment statement
assignstmt: expr ARROW expr ;
		
	// If statement
ifstmt: IF ifexpr stmt ((ELIF ifexpr stmt)* (ELSE stmt))?;
ifexpr: LPAREN expr RPAREN ;

	// For statement
forstmt: FOR IDENTIFIER UNTIL expr BY expr NEWLINE? stmt ;
	// Others
otherstmt: breakstmt | continuestmt | returnstmt | blockstmt ;
breakstmt: BREAK ;
continuestmt: CONTINUE ;
returnstmt: RETURN expr? ;
blockstmt: BEGIN NEWLINE? stmt*? NEWLINE? END ;

	// Function call statement
funccall: IDENTIFIER paramdecl | builtin;
paramdecl: LPAREN paramlist RPAREN;
paramlist: paramprime | ;
paramprime: param COMMA paramprime | param;
param: literals | funccall | IDENTIFIER | expr;

// Expressions
expr: expr1 ELLIPSIS expr1 | expr1;
expr1: expr2 relationals expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (PLUS | MINUS) expr4 | expr4;
expr4: expr4 (MULTIPLY | DIVIDE | MODULO) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: MINUS expr6 | expr7;
expr7: (IDENTIFIER | funccall) LBRACKET idxop RBRACKET | expr9; // expr7 is basically the representation of an array element
idxop: expr COMMA idxop | expr;
expr9: literals | LPAREN expr RPAREN | funccall | IDENTIFIER;

relationals: ASSIGN | EQUAL| NOT_EQUAL | LESS_THAN | GREATER_THAN | LESS_THAN_OR_EQUAL | GREATER_THAN_OR_EQUAL ;

typ : NUMBER | BOOL | STRING ;
literals : NUMBER_LITERAL | STRING_LITERAL | BOOL_LITERAL ;

//------------------------LEXER-----------------------------

// Literals

NUMBER_LITERAL: INT DOT? INT_PART? EXP_PART?;
fragment INT : [0-9]+ ;
fragment EXP_PART: [eE] [+-]? INT_PART ;
fragment INT_PART: [0-9]* ;
fragment DOT: [.] ;

BOOL_LITERAL: TRUE | FALSE;

STRING_LITERAL: ["] (~'\n' | ESCAPE_SEQUENCE | DOUBQ)* ["] 
{content = str(self.text)
self.text = content[1:-1]};
fragment ESCAPE_SEQUENCE: '\\' ( 'b' | 'f' | 'r' | 'n' | 't' | '\'' | '\\' ) ;
fragment DOUBQ: '\''["] ;

//	Keywords

TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
/*
NOT: 'not';
AND: 'and';
OR: 'or';
 */

// Operators
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MODULO: '%';
NOT: 'not';
AND: 'and';
OR: 'or';
ASSIGN: '=';
ARROW: '<-';
NOT_EQUAL: '!=';
LESS_THAN: '<';
LESS_THAN_OR_EQUAL: '<=';
GREATER_THAN: '>';
GREATER_THAN_OR_EQUAL: '>=';
ELLIPSIS: '...';
EQUAL: '==';

// Separators
COMMA: ',';
LPAREN: '(';
RPAREN: ')';
LBRACKET: '[';
RBRACKET: ']';

IDENTIFIER: [a-zA-Z_] [a-zA-Z_0-9]*;

WS : [ \t\b\f\n]+ -> skip ; // skip spaces, tabs, newlines
NEWLINE: '\r'? '\n';
COMMENT: '##' ~[\r\n]* ('\r'? '\n' | EOF) -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;