package tech.codealpha;

/**
 * String utility service.
 */
public class StringService {

    public String reverse(String input) {
        if (input == null) throw new IllegalArgumentException("Input must not be null");
        return new StringBuilder(input).reverse().toString();
    }

    public boolean isPalindrome(String input) {
        if (input == null) throw new IllegalArgumentException("Input must not be null");
        String cleaned = input.toLowerCase().replaceAll("[^a-z0-9]", "");
        return cleaned.equals(new StringBuilder(cleaned).reverse().toString());
    }

    public int countWords(String input) {
        if (input == null || input.isBlank()) return 0;
        return input.trim().split("\\s+").length;
    }

    public String capitalize(String input) {
        if (input == null || input.isEmpty()) return input;
        return Character.toUpperCase(input.charAt(0)) + input.substring(1).toLowerCase();
    }

    public String repeat(String input, int times) {
        if (times < 0) throw new IllegalArgumentException("Times must be non-negative");
        return input.repeat(times);
    }
}
