/*
 * Lexer Rules
 */

grammar Typescript;

TRUE          : 'true';
FALSE         : 'false';
DOT           : '.';
COLON         : ':';
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
FUNCTION      : 'function';
STRING        : 'string';
NUMBER        : 'number';
BOOLEAN       : 'boolean';


IDENTIFIER : Letter LetterOrDigit*;
CHARS      : ('"' StringCharacter* '"') | ('\'' CharSequence* '\'');
DIGITS     : Digit+((DOT)Digit+)?;

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
sAll            : (sExpression | sTerm | sInvocation | sValue | sIf | sReturn | sFunction | sOverloading)* EOF;
sOperand        : sNumber | sProperty | sInvocation;
sOperator       : sPlus | sMinus | sMul | sDiv | sPower;
sExpression     : sArithmeticExpression | sBooleanExpression | sNumberExpression | sStringExpression;
sTerm           : sArithmeticTerm | sBooleanTerm;
sValue          : sNumber | sBoolean | sString | sArray | sMap;
sInvocation     : sPropertyAccess | sFunctionAccess | sFunctionCall;
sOverloading    : (sValue | sProperty) (PLUS (sValue | sProperty))+;

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
sBooleanOperand    : sValue | sProperty;
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
sStringOverloading : sString (PLUS sString)+;

sType              : STRING | NUMBER | BOOLEAN;

// function definition
// *******************
sFunction          : sFunctionHead sFunctionTail;
sFunctionArg       : sValue | sOverloading | sExpression;
sFunctionArgs      : sFunctionArg (COMMA sFunctionArg)*;
sFunctionArgDef    : sProperty (COLON sType)?;
sFunctionArgDefs   : sFunctionArgDef (COMMA sFunctionArgDef)*;
sFunctionHead      : FUNCTION IDENTIFIER ROUND_LEFT sFunctionArgDefs? ROUND_RIGHT (COLON sType)?;
sFunctionTail      : CURLY_LEFT sBody CURLY_RIGHT;
sFunctionCall      : IDENTIFIER ROUND_LEFT sFunctionArgs? ROUND_RIGHT;

sProperty          : IDENTIFIER;
sPropertyAware     : sString | sProperty;
sPropertyAccess    : sPropertyAware ((DOT sProperty) | (BRACKET_LEFT sNumber BRACKET_RIGHT))+;

sFunctionAware     : sString | sProperty;
sFunctionAccess    : sFunctionAware (DOT sFunctionCall)+;

sBody              : (sIf)* sReturn?;
sReturn            : RETURN (sValue | sExpression | sOverloading | sProperty | sInvocation);

// if parser rules
// ***************
sIf      : IF ROUND_LEFT sExpression ROUND_RIGHT (sReturn | (CURLY_LEFT sBody CURLY_RIGHT)) sElseIf* sElse?;
sElse    : ELSE (sReturn | (CURLY_LEFT sBody CURLY_RIGHT));
sElseIf  : ELSE IF ROUND_LEFT sBooleanExpression ROUND_RIGHT (sReturn | (CURLY_LEFT sBody CURLY_RIGHT));

// value definitions
// *****************
sString         : CHARS;
sNumber         : DIGITS;
sBoolean        : TRUE | FALSE;
sArray          : BRACKET_LEFT (sValue (COMMA sValue)*)? BRACKET_RIGHT;
sMap            : CURLY_LEFT (sString COLON sValue (COMMA sString COLON sValue)*)? CURLY_RIGHT;