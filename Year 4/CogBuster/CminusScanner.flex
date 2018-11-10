/* A scanner for C-- programming language */

%%
%class CminusScanner
%function nextToken
%type CminusToken

/* DEFINITIONS */

digit = [0-9]
letter = [a-zA-Z]
number = {digit}+
identifier = {letter}+
newline = \n
whitespace = [ \t]+

%%

/* RULES */

/* reserved words */
"if" { return new CminusToken(CminusToken.TokenKind.RW_IF); }
"else" { return new CminusToken(CminusToken.TokenKind.RW_ELSE); }
"int" { return new CminusToken(CminusToken.TokenKind.RW_INT); }
"return" { return new CminusToken(CminusToken.TokenKind.RW_RETURN); }
"void" { return new CminusToken(CminusToken.TokenKind.RW_VOID); }
"while" { return new CminusToken(CminusToken.TokenKind.RW_WHILE); }

/* operators */
"=" { return new CminusToken(CminusToken.TokenKind.SYM_ASSIGN); }
"==" { return new CminusToken(CminusToken.TokenKind.SYM_EQ); }
"!=" { return new CminusToken(CminusToken.TokenKind.SYM_NOTEQ); } 
">" { return new CminusToken(CminusToken.TokenKind.SYM_GT); } 
"<" { return new CminusToken(CminusToken.TokenKind.SYM_LT); } 
">=" { return new CminusToken(CminusToken.TokenKind.SYM_GTEQ); } 
"<=" { return new CminusToken(CminusToken.TokenKind.SYM_LTEQ); } 
"+" { return new CminusToken(CminusToken.TokenKind.SYM_PLUS); } 
"-" { return new CminusToken(CminusToken.TokenKind.SYM_MINUS); }
"*" { return new CminusToken(CminusToken.TokenKind.SYM_TIMES); } 
"/" { return new CminusToken(CminusToken.TokenKind.SYM_OVER); } 

"(" { return new CminusToken(CminusToken.TokenKind.SYM_LPAREN); } 
")" { return new CminusToken(CminusToken.TokenKind.SYM_RPAREN); } 
"[" { return new CminusToken(CminusToken.TokenKind.SYM_LSQR);} 
"]" { return new CminusToken(CminusToken.TokenKind.SYM_RSQR); } 
"{" { return new CminusToken(CminusToken.TokenKind.SYM_LCURL); } 
"}" { return new CminusToken(CminusToken.TokenKind.SYM_RCURL); } 
";" { return new CminusToken(CminusToken.TokenKind.SYM_SEMI); } 
"," { return new CminusToken(CminusToken.TokenKind.SYM_COMMA); }

{number} { return new CminusToken(CminusToken.TokenKind.NUMBER); }
{identifier} { return new CminusToken(CminusToken.TokenKind.ID); }    

{whitespace} { /* skip whitespace */ }
\{[^}]*\} { /* skip comments */ }
{newline} { /* skip newline */ }
.
{ return new CminusToken(CminusToken.TokenKind.ILLEGAL); }