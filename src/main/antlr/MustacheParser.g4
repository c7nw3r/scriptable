/*
 * Lexer Rules
 */

parser grammar MustacheParser;

options { tokenVocab=MustacheLexer; }

/*
 * Parser Rules
 */
sAll            : (sTag | sProperty | sText)* EOF;

// operator definitions
// ********************
sTagStart       : OPEN_TAG_START PROPERTY_TAG_START CLOSE_TAG_START;
sTagEnd         : OPEN_TAG_END PROPERTY_TAG_END CLOSE_TAG_END;
sTag            : sTagStart (sText | sProperty)* sTagEnd;
sProperty       : OPEN PROPERTY CLOSE;
sText           : TEXT;
