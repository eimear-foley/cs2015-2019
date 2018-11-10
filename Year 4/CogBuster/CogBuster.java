import java.io.File;
import java.io.FilenameFilter;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * Extracts the Profiles of C-- programs
 * Computes the measure of distance between Profile pairs
 * Flags pairs that are less than some specified threshold
 * @author Eimear Foley
 */
class CogBuster {
    private static final Double THRESHOLD = 0.05;

    /**
     * Flags files in the directory 'path' that are potentially plagiarised
     * Files within a distance threshold of 0.05 are said to be 'cogged'
     * @param path - name of a directory
     * @throws IOException
     */
    public CogBuster(String path) throws IOException {

        if (path != null && !path.isEmpty()) {

            File directory = new File(path);
            Map<File, Profile> profileMap = new HashMap<>();

            /* Create a Profile of only C-- files */
            FilenameFilter filter = new FilenameFilter() {
                @Override
                public boolean accept(File dir, String name) {
                    if (name.endsWith(".c")) {
                        return true;
                    }
                    return false;
                }
            };

            for (File file : directory.listFiles(filter)) {
                Profile profile = new Profile(file);
                profileMap.put(file, profile);
            }

            Set<String> flaggedFiles = new HashSet<>();

            try {
                for (Map.Entry<File, Profile> entry : profileMap.entrySet()) {
                    for (File f : profileMap.keySet()) {
                        if (!entry.getKey().equals(f)) {
                            Double distance = entry.getValue().compare(f);
                            if (distance < THRESHOLD) {
                                flaggedFiles.add(f.getName());
                                flaggedFiles.add(entry.getKey().getName());
                            }
                        }
                    }
                }
            } catch (IOException e) {
                throw new IOException("File handler error.");
            }

            System.out.println("**** FLAGGED FILES ****");
            for (String s : flaggedFiles) {
                System.out.println(s);
            }

        } else {
            throw new IllegalArgumentException("Null directory path received.");
        }
    }

    /**
     * Main function for testing our CogBuster program
     * @param args - default
     * @throws IOException
     */
    public static void main(String[] args) throws IOException {
        CogBuster cogBuster = new CogBuster("test");
    }
}
