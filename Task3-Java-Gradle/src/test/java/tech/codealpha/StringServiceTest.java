package tech.codealpha;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("StringService Tests")
class StringServiceTest {

    private StringService str;

    @BeforeEach
    void setUp() { str = new StringService(); }

    // ── reverse
    @Test
    void testReverse() { assertEquals("olleh", str.reverse("hello")); }

    @Test
    void testReverseNull() {
        assertThrows(IllegalArgumentException.class, () -> str.reverse(null));
    }

    @Test
    void testReverseEmpty() { assertEquals("", str.reverse("")); }

    @Test
    void testReverseSingleChar() { assertEquals("a", str.reverse("a")); }

    // ── isPalindrome
    @Test
    void testIsPalindromeTrue() { assertTrue(str.isPalindrome("racecar")); }

    @Test
    void testIsPalindromeFalse() { assertFalse(str.isPalindrome("hello")); }

    @Test
    void testIsPalindromeWithSpaces() { assertTrue(str.isPalindrome("A man a plan a canal Panama")); }

    // ── countWords
    @Test
    void testCountWords() { assertEquals(2, str.countWords("hello world")); }

    @Test
    void testCountWordsEmpty() { assertEquals(0, str.countWords("")); }

    @Test
    void testCountWordsMultipleSpaces() { assertEquals(3, str.countWords("one  two   three")); }

    // ── capitalize
    @Test
    void testCapitalize() { assertEquals("Hello", str.capitalize("hello")); }

    @Test
    void testCapitalizeAlreadyUpper() { assertEquals("Hello", str.capitalize("HELLO")); }

    @Test
    void testCapitalizeEmpty() { assertEquals("", str.capitalize("")); }

    // ── repeat
    @Test
    void testRepeat() { assertEquals("abcabc", str.repeat("abc", 2)); }

    @Test
    void testRepeatZero() { assertEquals("", str.repeat("abc", 0)); }

    @Test
    void testRepeatNegativeThrows() {
        assertThrows(IllegalArgumentException.class, () -> str.repeat("abc", -1));
    }
}
