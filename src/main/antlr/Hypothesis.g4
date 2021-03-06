/*
 * Lexer Rules
 */

grammar Hypothesis;

TRUE          : 'true';
FALSE         : 'false';
DOT           : '.';
COLON         : ':';
COMMA         : ',';
SEMICOLON     : ';';
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
ARROW         : '=>';
WHILE         : 'while';
FOR           : 'for';
IN            : 'in';
OF            : 'of';
CONST         : 'const';
VAR           : 'var';
LET           : 'let';
EQUAL         : '=';
BREAK         : 'break';
CONTINUE      : 'continue';


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

/*
 * Parser Rules
 */
sAll            : sExpression EOF;
sOperand        : sNumber | sProperty | sPropertyAccess;
sOperator       : sPlus | sMinus | sMul | sDiv | sPower;
sExpression     : sConcatExpression | sArithmeticExpression | sBooleanExpression | sNumberExpression | sStringExpression;
sTerm           : sArithmeticTerm | sBooleanTerm;
sValue          : sNumber | sBoolean | sString | sArray | sMap;

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
sEquals         : EQ | STRICT_EQ;
sNotEquals      : NEQ | STRICT_NEQ;
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
sBooleanOperand    : sValue | sProperty | sPropertyAccess;
sBooleanOperator   : sAnd | sOr | sNot | sEquals | sNotEquals;
sBooleanExpression : (sBooleanOperand | sBooleanTerm) (sBooleanOperator (sBooleanOperand | sBooleanTerm))*;
sBooleanTerm       : ROUND_LEFT ((sBooleanOperand (sBooleanOperator sBooleanOperand)+) | sBooleanTerm) ROUND_RIGHT;

// number expression
// *****************
sNumberOperand     : sNumber | sProperty | sPropertyAccess;
sNumberOperator    : sEquals | sNotEquals | sLowerThan | sLowerEquals | sGreaterThan | sGreaterEquals;
sNumberExpression  : (sNumberOperand | sNumberTerm) (sNumberOperator (sNumberOperand | sNumberTerm))+;
sNumberTerm        : ROUND_LEFT ((sNumberOperand (sNumberOperator sNumberOperand)+) | sNumberTerm) ROUND_RIGHT;

// string expression
// *****************
sStringOperand     : sString;
sStringOperator    : sEquals | sNotEquals;
sStringExpression  : (sStringOperand | sStringTerm) (sStringOperator (sStringOperand | sStringTerm))+;
sStringTerm        : ROUND_LEFT ((sStringOperand (sStringOperator sStringOperand)+) | sStringTerm) ROUND_RIGHT;

// concat expression
sConcatOperand     : sString;
sConcatExpression  : sConcatBoth | sConcatLeft | sConcatRight;
sConcatLeft        : sString sPlus (sValue | sProperty);
sConcatRight       : (sValue | sProperty) sPlus sString;
sConcatBoth        : sString (sPlus sString)+;

sType              : STRING | NUMBER | BOOLEAN;

sProperty          : IDENTIFIER;
sPropertyAware     : sString | sProperty;
sPropertyAccess    : sPropertyAware ((DOT sProperty) | (BRACKET_LEFT (sNumber | sString) BRACKET_RIGHT))+;

// value definitions
// *****************
sString  : CHARS;
sNumber  : DIGITS;
sBoolean : TRUE | FALSE;
sArray   : BRACKET_LEFT (sValue (COMMA sValue)*)? BRACKET_RIGHT;
sMap     : CURLY_LEFT (sString COLON sValue (COMMA sString COLON sValue)*)? CURLY_RIGHT;
