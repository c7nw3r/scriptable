/*
 * Lexer Rules
 */

grammar Typescript;

TRUE          : 'true';
FALSE         : 'false';
DOT           : '.';
COMMA         : ',';
PLUS          : '+';
MINUS         : '-';
MUL           : '*';
DIV           : '/';
POWER         : '**';
ROUND_LEFT    : '(';
ROUND_RIGHT   : ')';
CURLY_LEFT    : '{';
CURLY_RIGHT   : '}';
BRACKET_LEFT  : '[';
BRACKET_RIGHT : ']';
AND           : '&&';
OR            : '||';
NOT           : '!';
EQ            : '==';
STRICT_EQ     : '===';
NEQ           : '!=';
STRICT_NEQ    : '!==';
LT            : '<';
LE            : '<=';
GT            : '>';
GE            : '>=';
IF            : 'if';
ELSE          : 'else';
RETURN        : 'return';

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
sAll            : (sExpression | sTerm | sValue | sInvocation | sIf | sReturn)* EOF;
sOperand        : sNumber;
sOperator       : sPlus | sMinus | sMul | sDiv | sPower;
sExpression     : sArithmeticExpression | sBooleanExpression | sNumberExpression | sStringExpression;
sTerm           : sArithmeticTerm | sBooleanTerm;
sValue          : sNumber | sBoolean | sString;
sInvocation     : sPropertyAccess | sFunctionAccess;

// value definitions
// *****************
sString         : CHARS;
sNumber         : NUMBER;
sBoolean        : TRUE | FALSE;

// operator definitions
// ********************
sPlus           : PLUS;
sMinus          : MINUS;
sMul            : MUL;
sDiv            : DIV;
sPower          : POWER;
sAnd            : AND;
sOr             : OR;
sNot            : NOT;
sEquals         : EQ || STRICT_EQ;
sNotEquals      : NEQ || STRICT_NEQ;
sLowerThan      : LT;
sLowerEquals    : LE;
sGreaterThan    : GT;
sGreaterEquals  : GE;

// arithmetic expression
// *********************
sArithmeticExpression : (sOperand | sArithmeticTerm) (sOperator (sOperand | sArithmeticTerm))+;
sArithmeticTerm       : ROUND_LEFT ((sOperand (sOperator sOperand)+) | sArithmeticTerm) ROUND_RIGHT;

// boolean expression
// ******************
sBooleanOperand    : sBoolean;
sBooleanOperator   : sAnd | sOr | sNot | sEquals | sNotEquals;
sBooleanExpression : (sBooleanOperand | sBooleanTerm) (sBooleanOperator (sBooleanOperand | sBooleanTerm))*;
sBooleanTerm       : ROUND_LEFT ((sBooleanOperand (sBooleanOperator sBooleanOperand)+) | sBooleanTerm) ROUND_RIGHT;

// number expression
// *****************
sNumberOperand     : sNumber;
sNumberOperator    : sEquals | sNotEquals | sLowerThan | sLowerEquals | sGreaterThan | sGreaterEquals;
sNumberExpression  : (sNumberOperand | sNumberTerm) (sNumberOperator (sNumberOperand | sNumberTerm))+;
sNumberTerm        : ROUND_LEFT ((sNumberOperand (sNumberOperator sNumberOperand)+) | sNumberTerm) ROUND_RIGHT;

// string expression
// *****************
sStringOperand     : sString;
sStringOperator    : sEquals | sNotEquals;
sStringExpression  : (sStringOperand | sStringTerm) (sStringOperator (sStringOperand | sStringTerm))+;
sStringTerm        : ROUND_LEFT ((sStringOperand (sStringOperator sStringOperand)+) | sStringTerm) ROUND_RIGHT;

// function definition
// *******************
sFunctionArg       : sValue;
sFunctionCall      : IDENTIFIER ROUND_LEFT (sFunctionArg (COMMA sFunctionArg)*)? ROUND_RIGHT;

sProperty          : IDENTIFIER;
sPropertyAware     : sString | sProperty;
sPropertyAccess    : sPropertyAware ((DOT sProperty) | (BRACKET_LEFT sNumber BRACKET_RIGHT))+;

sFunctionAware     : sString | sProperty;
sFunctionAccess    : sFunctionAware (DOT sFunctionCall)+;

sBody              : (sIf)* sReturn?;
sReturn            : RETURN sValue;

// if parser rules
// ***************
sIf      : IF ROUND_LEFT sBooleanExpression ROUND_RIGHT (sReturn | (CURLY_LEFT sBody CURLY_RIGHT)) sElseIf* sElse?;
sElse    : ELSE (sReturn | (CURLY_LEFT sBody CURLY_RIGHT));
sElseIf  : ELSE IF ROUND_LEFT sBooleanExpression ROUND_RIGHT (sReturn | (CURLY_LEFT sBody CURLY_RIGHT));