/*
 * Lexer Rules
 */

grammar Typescript;

TRUE          : 'true';
FALSE         : 'false';
DOT           : '.';
PLUS          : '+';
MINUS         : '-';
MUL           : '*';
DIV           : '/';
ROUND_LEFT    : '(';
ROUND_RIGHT   : ')';
AND           : '&&';
OR            : '||';
NOT           : '!';

IDENTIFIER : Letter LetterOrDigit*;
CHARS      : ('"' StringCharacter* '"') | ('\'' CharSequence* '\'');
NUMBER     : Digit+((DOT)Digit+)?;

fragment Digit           : '-'?[0-9];
fragment Letter          : [a-zA-Z];
fragment LetterOrDigit   : [a-zA-Z0-9_];
fragment StringCharacter :	~'"';
fragment CharSequence    :	~'\'';

//
// Whitespace and comments
//
WS           : [ \t\r\n\u000C]+ -> skip;
LINE_COMMENT : '//' ~[\r\n]*    -> skip;
WHITESPACE   : ' '              -> skip;
SEMICOLON    : ';'              -> skip;

/*
 * Parser Rules
 */
sAll            : (sExpression | sTerm)* EOF;
sNumber         : NUMBER;
sOperand        : sNumber;
sOperator       : sPlus | sMinus | sMul | sDiv | sPower;
sExpression     : sArithmeticExpression | sLogicExpression;

// arithmetic expression
// *********************
sArithmeticExpression : (sOperand | sTerm) (sOperator (sOperand | sTerm))+;
sTerm                 : ROUND_LEFT sOperand (sOperator sOperand)+ ROUND_RIGHT;
sPlus : PLUS;
sMinus : MINUS;
sMul : MUL;
sDiv : DIV;
sPower : POWER;

// logic expression
// ****************
sLogicOperator   : sAnd | sOr | sNot;
sLogicExpression : sLogicOperand (sLogicOperator sLogicOperand)+;
sAnd             : AND;
sOr              : OR;
sNot             : NOT;
sBoolean         : TRUE | FALSE;
sLogicOperand    : sBoolean;
