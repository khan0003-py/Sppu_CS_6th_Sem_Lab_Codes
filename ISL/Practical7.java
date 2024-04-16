import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Practical7 {
    public static void main(String[] args) {
        String text = "Hello, world!";
        try {
            // Create MessageDigest instance for MD5
            MessageDigest md = MessageDigest.getInstance("MD5");
            // Update digest with input text
            md.update(text.getBytes());
            // Calculate digest (hash) value
            byte[] digest = md.digest();
            // Convert byte array to hexadecimal string
            StringBuilder sb = new StringBuilder();
            for (byte b : digest) {
                sb.append(String.format("%02x", b & 0xff));
            }
            // Print the MD5 hash
            System.out.println("MD5 Hash of \"" + text + "\": " + sb.toString());
        } catch (NoSuchAlgorithmException e) {
            System.out.println("MD5 algorithm not found.");
            e.printStackTrace();
        }
    }
}