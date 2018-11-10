/**
 * Class to represent individual tokens found in a C-- program
 * @author Eimear Foley
 */
public class CminusToken {
    /* Classification of this token */
    private TokenKind kind;
    /* Numerical value of this token; valid only for NUMBER tokens */
    private int value;
    /* Spelling of this token */
    private String spelling;

    /**
     * Creates a CminusToken of the specified TokenKind
     * @param k - the required token kind
     */
    public CminusToken(TokenKind k) {
        kind = k;
    }

    /**
     * Creates a NUMBER token kind from a specified value
     * @param v - value of NUMBER token kind
     */
    public CminusToken (int v) {
        kind = TokenKind.NUMBER;
        value = v;
    }

    /**
     * Creates a ID token kind from a specified spelling
     * @param sp - spelling of ID token kind
     */
    public CminusToken (String sp) {
        kind = kind.ID;
        spelling = sp;
    }

    /**
     * Returns type of a token e.g. NUMBER
     * @return type of token
     */
    public TokenKind getKind() {
        return kind;
    }

    /**
     * Returns the spelling of a ID token kind
     * @return spelling of a token
     */
    public String getSpelling() {
        return spelling;
    }

    /**
     * Returns the values of a NUMBER token
     * @return an integer value of a token
     */
    public int getValue() {
        return value;
    }

    /**
     * Returns the spring representation of a token
     * @return the string representation of a token
     */
    public String toString()
    {  String str = kind.toString();
        switch (kind)
        {
            case NUMBER    :
                str += "["+value+"]";
                break;
            case ID    :
                str += "["+spelling+"]";
                break;
        }
        return str;
    }

    /**
     * Enum representing the unique tokens of the C-- programming language
     */
    public enum TokenKind {

        RW_IF,
        RW_ELSE,
        RW_INT,
        RW_RETURN,
        RW_VOID,
        RW_WHILE,

        SYM_ASSIGN, // =
        SYM_EQ,     // ==
        SYM_NOTEQ,  // !=
        SYM_GT,     // >
        SYM_GTEQ,   // >=
        SYM_LTEQ,   // <=
        SYM_LT,     // <
        SYM_PLUS,   // +
        SYM_MINUS,  // -
        SYM_TIMES,  // *
        SYM_OVER,   // /
        SYM_LPAREN, // (
        SYM_RPAREN, // )
        SYM_LSQR,   // [
        SYM_RSQR,   // ]
        SYM_LCURL,  // {
        SYM_RCURL,  // }
        SYM_COMMA,  // ,
        SYM_SEMI,   // ;

        NUMBER,
        ID,

        ILLEGAL
    }

}
