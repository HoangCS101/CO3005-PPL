grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: NEWLINE*? main_stmt (NEWLINE+ main_stmt)* NEWLINE+ EOF;

// Statements
main_stmt: ( vardecl | var_vardecl | funcdecl);
stmt: (
		vardecl
		| var_vardecl
		| builtin
		| funccall
		| assignstmt
		| ifstmt
		| forstmt
		| otherstmt
		| expr
	);

// // Declarations Variable declaration vardecl: typ IDENTIFIER (ARROW expr | ARROW array)?; //
// expr7 is for IDENTIFIER + index operator, which is an array element, for example : a[5]
// im_vardecl: VAR IDENTIFIER (ARROW expr | ARROW array); im_dydecl: DYNAMIC IDENTIFIER (ARROW expr
// | ARROW array)?;

// Function declaration
funcdecl: FUNC IDENTIFIER arg funcend?;
arg: LPAREN arglist RPAREN;
arglist: argprime |;
argprime: argment COMMA argprime | argment;
argment: vardecl;
funcend: NEWLINE* ( returnstmt | blockstmt);

// Built-in function
builtin:
	readnum
	| writenum
	| readbool
	| writebool
	| readstr
	| writestr;
readnum: 'readNumber' LPAREN RPAREN;
writenum: 'writeNumber' LPAREN expr RPAREN;
readbool: 'readBool' LPAREN RPAREN;
writebool: 'writeBool' LPAREN expr RPAREN;
readstr: 'readString' LPAREN RPAREN;
writestr: 'writeString' LPAREN expr RPAREN;

// Array declaration
vardecl:
	(typ | DYNAMIC) IDENTIFIER (LBRACKET arraydim RBRACKET)? (
		ARROW array
		| ARROW expr
	)?;
var_vardecl:
	VAR IDENTIFIER (LBRACKET arraydim RBRACKET)? (
		ARROW array
		| ARROW expr
	);
arraydim: NUMBER_LITERAL (COMMA NUMBER_LITERAL)*;
array: LBRACKET arrayelement (COMMA arrayelement)* RBRACKET;
arrayelement: expr | array;

// Assignment statement
assignstmt: expr ARROW expr;

// If statement
ifstmt: IF expr NEWLINE* stmt elifstmt elsestmt;
elifstmt: NEWLINE ELIF expr NEWLINE* stmt elifstmt |;
elsestmt: NEWLINE ELSE stmt |;

// For statement
forstmt: FOR IDENTIFIER UNTIL expr BY expr NEWLINE? stmt;

// Others
otherstmt: breakstmt | continuestmt | returnstmt | blockstmt;
breakstmt: BREAK;
continuestmt: CONTINUE;
returnstmt: RETURN expr?;
blockstmt: BEGIN NEWLINE (stmt (NEWLINE stmt)* |) NEWLINE END;

// Function call statement
funccall: IDENTIFIER LPAREN paramlist RPAREN | builtin;
paramlist: paramprime |;
paramprime: expr COMMA paramprime | expr;

// Expressions
expr: expr1 ELLIPSIS expr1 | expr1;
expr1: expr2 relationals expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (PLUS | MINUS) expr4 | expr4;
expr4: expr4 (MULTIPLY | DIVIDE | MODULO) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: MINUS expr6 | expr7;
expr7: (IDENTIFIER | funccall) LBRACKET expr8 RBRACKET
	| expr9; // expr7 is basically the representation of an array element
expr8: expr COMMA expr8 | expr;
expr9: literals | LPAREN expr RPAREN | funccall | IDENTIFIER;

relationals:
	ASSIGN
	| EQUAL
	| NOT_EQUAL
	| LESS_THAN
	| GREATER_THAN
	| LESS_THAN_OR_EQUAL
	| GREATER_THAN_OR_EQUAL;

typ: NUMBER | BOOL | STRING;
literals: NUMBER_LITERAL | STRING_LITERAL | BOOL_LITERAL;

//------------------------LEXER-----------------------------

// Literals
NUMBER_LITERAL: INT DOT? INT_PART? EXP_PART?;
fragment INT: [0-9]+;
fragment EXP_PART: [eE] [+-]? INT_PART;
fragment INT_PART: [0-9]*;
fragment DOT: [.];

BOOL_LITERAL: TRUE | FALSE;

STRING_LITERAL:
	["] (STR_CHAR | ESCAPE_SEQUENCE | DOUBQ)* ["] {
	self.text = str(self.text)[1:-1]
};
fragment STR_CHAR: ~[\\"\n];
fragment ESCAPE_SEQUENCE:
	'\\' ('b' | 'f' | 'r' | 'n' | 't' | '\'' | '\\');
fragment DOUBQ: '\'' ["];
fragment ESCAPE_ERROR: '\\' ~[bfrnt'\\] | '\'' ~'"';

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
 NOT: 'not'; AND: 'and'; OR: 'or';
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

WS: [ \t\b\f]+ -> skip;
NEWLINE: '\n' | '\r' | '\r\n';
COMMENT: '##' ~[\r\n]* -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING:
	'"' (STR_CHAR | ESCAPE_SEQUENCE)* (EOF | '\n') {
	content = str(self.text)
	esc = '\n'
	if content[-1] in esc:
		raise UncloseString(content[1:-1])
	else:
		raise UncloseString(content[1:])
};
ILLEGAL_ESCAPE:
	'"' (STR_CHAR | ESCAPE_SEQUENCE)* ESCAPE_ERROR {
	raise IllegalEscape(str(self.text)[1:])
};