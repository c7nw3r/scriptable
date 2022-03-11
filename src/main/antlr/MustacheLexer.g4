/*
 * Lexer Rules
 */

lexer grammar MustacheLexer;

// default mode: everything OUTSIDE a mustache instruction
// *******************************************************
TEXT           : (~'{')+;
OPEN_TAG_START : '{{#' -> pushMode(MUSTACHE_TAG_START);
OPEN_TAG_END   : '{{/' -> pushMode(MUSTACHE_TAG_END);
OPEN           : '{{' -> pushMode(MUSTACHE);

fragment Letter          : [a-zA-Z];
fragment LetterOrDigit   : [a-zA-Z0-9_];

// mustache mode: everything INSIDE a mustache instruction
// *******************************************************
mode MUSTACHE;
PROPERTY: (Letter LetterOrDigit*) | '.';
CLOSE : '}}' {print("CLOSE")} -> popMode;

mode MUSTACHE_TAG_START;
PROPERTY_TAG_START: Letter LetterOrDigit*;
CLOSE_TAG_START : '}}' -> popMode;

mode MUSTACHE_TAG_END;
PROPERTY_TAG_END: Letter LetterOrDigit*;
CLOSE_TAG_END : '}}' -> popMode;