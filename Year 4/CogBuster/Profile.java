import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

/**
 * Embodies a 'profile' of a C-- language program.
 * Computes the measure of distance between one profile and another.
 * @author Eimear Foley
 */
class Profile {
    private Map<String, Double> tokenRecord = new HashMap<>();
    private File f;

    /**
     * Constructor for Profile class, takes one argument
     * @param f - a File object
     */
    public Profile(File f) {
        this.f = f;
    }

    /**
     * Analyses the contents of a Profile using the CminusScanner
     * Records each unique token type and its frequency for each Profile
     * @return Hash map of unique tokens as Strings and frequencies as Doubles
     * @throws IOException
     */
    public Map<String, Double> analyse() throws IOException {
        try {
            CminusScanner scanner = new CminusScanner(new FileReader(f));
            CminusToken currentToken = scanner.nextToken();

            while (currentToken != null) {
                if (tokenRecord.get(currentToken.toString()) == null) {
                    tokenRecord.put(currentToken.toString(), 1.0);
                }
                else {
                    tokenRecord.put(currentToken.toString(), tokenRecord.get(currentToken.toString()) + 1.0);
                }
                currentToken = scanner.nextToken();
            }
        } catch (IOException e) {
            throw new IOException("Error handling file.");
        }
        return tokenRecord;
    }

    /**
     * Compares the Profile of one file with the Profile of another file
     * @param other - a File object to compare against
     * @return the distance between the two Profiles as a Double
     * @throws IOException
     */
    public Double compare(File other) throws IOException {
        tokenRecord = analyse();
        Profile otherProfile = new Profile(other);
        Map<String, Double> otherTokens = otherProfile.analyse();

        double aMinusB = 0.0;
        double aValues = 0.0;
        double bValues = 0.0;

        for (Entry<String, Double> entry : tokenRecord.entrySet()) {
            if (!otherTokens.containsKey(entry.getKey())) {
                otherTokens.put(entry.getKey(), 0.0);
            }
        }

        Map<String, Double> tokenRecordCopy = tokenRecord;

        for (Entry<String, Double> entry : otherTokens.entrySet()) {
            if (!tokenRecord.containsKey(entry.getKey())) {
                tokenRecordCopy.put(entry.getKey(), 0.0);
            }
        }

        for (String token : tokenRecordCopy.keySet()) {
            aMinusB += Math.pow(tokenRecordCopy.get(token) - otherTokens.get(token), 2);
            aValues += Math.pow(tokenRecordCopy.get(token), 2);
            bValues += Math.pow(otherTokens.get(token), 2);
        }

        return ((Math.sqrt(aMinusB) / ((Math.sqrt(aValues)) * (Math.sqrt(bValues)))));
    }

}