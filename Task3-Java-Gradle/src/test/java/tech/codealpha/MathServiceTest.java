package tech.codealpha;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("MathService Tests")
class MathServiceTest {

    private MathService math;

    @BeforeEach
    void setUp() { math = new MathService(); }

    // ── add
    @Test
    @DisplayName("add: positive numbers")
    void testAddPositive() { assertEquals(8.0, math.add(3, 5)); }

    @Test
    @DisplayName("add: negative numbers")
    void testAddNegative() { assertEquals(-8.0, math.add(-3, -5)); }

    @Test
    @DisplayName("add: with zero")
    void testAddZero() { assertEquals(5.0, math.add(5, 0)); }

    // ── subtract
    @Test
    @DisplayName("subtract: basic")
    void testSubtract() { assertEquals(5.0, math.subtract(10, 5)); }

    // ── multiply
    @Test
    @DisplayName("multiply: positive")
    void testMultiply() { assertEquals(12.0, math.multiply(4, 3)); }

    @Test
    @DisplayName("multiply: by zero")
    void testMultiplyByZero() { assertEquals(0.0, math.multiply(5, 0)); }

    // ── divide
    @Test
    @DisplayName("divide: basic")
    void testDivide() { assertEquals(2.5, math.divide(5, 2)); }

    @Test
    @DisplayName("divide: by zero throws")
    void testDivideByZero() {
        assertThrows(ArithmeticException.class, () -> math.divide(10, 0));
    }

    // ── factorial
    @ParameterizedTest
    @DisplayName("factorial: parameterized")
    @CsvSource({
        "0, 1",
        "1, 1",
        "5, 120",
        "10, 3628800"
    })
    void testFactorial(int n, long expected) {
        assertEquals(expected, math.factorial(n));
    }

    @Test
    @DisplayName("factorial: negative throws")
    void testFactorialNegative() {
        assertThrows(IllegalArgumentException.class, () -> math.factorial(-1));
    }

    // ── isPrime
    @Test
    @DisplayName("isPrime: prime number")
    void testIsPrimeTrue() { assertTrue(math.isPrime(17)); }

    @Test
    @DisplayName("isPrime: composite number")
    void testIsPrimeFalse() { assertFalse(math.isPrime(15)); }

    @Test
    @DisplayName("isPrime: one is not prime")
    void testIsPrimeOne() { assertFalse(math.isPrime(1)); }

    @Test
    @DisplayName("isPrime: two is prime")
    void testIsPrimeTwo() { assertTrue(math.isPrime(2)); }

    // ── fibonacci
    @ParameterizedTest
    @DisplayName("fibonacci: parameterized")
    @CsvSource({
        "0, 0",
        "1, 1",
        "5, 5",
        "10, 55"
    })
    void testFibonacci(int n, long expected) {
        assertEquals(expected, math.fibonacci(n));
    }

    @Test
    @DisplayName("fibonacci: negative throws")
    void testFibonacciNegative() {
        assertThrows(IllegalArgumentException.class, () -> math.fibonacci(-1));
    }
}
