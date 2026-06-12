package tech.codealpha;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Main entry point for the CodeAlpha Java Gradle application.
 * Task 3: Java Application using Gradle.
 *
 * @author Marwan Tamer
 * @version 1.0.0
 */
public class App {

    private static final Logger log = LoggerFactory.getLogger(App.class);

    public static void main(String[] args) {
        log.info("CodeAlpha DevOps Internship - Task 3: Java Application using Gradle");

        MathService mathService = new MathService();
        StringService stringService = new StringService();

        // Demonstrate MathService
        log.info("--- MathService Demo ---");
        log.info("add(10, 5)      = {}", mathService.add(10, 5));
        log.info("subtract(10, 5) = {}", mathService.subtract(10, 5));
        log.info("multiply(4, 3)  = {}", mathService.multiply(4, 3));
        log.info("divide(10, 4)   = {}", mathService.divide(10, 4));
        log.info("factorial(5)    = {}", mathService.factorial(5));
        log.info("isPrime(17)     = {}", mathService.isPrime(17));
        log.info("fibonacci(10)   = {}", mathService.fibonacci(10));

        // Demonstrate StringService
        log.info("--- StringService Demo ---");
        log.info("reverse('hello')         = {}", stringService.reverse("hello"));
        log.info("isPalindrome('racecar')  = {}", stringService.isPalindrome("racecar"));
        log.info("countWords('hello world')= {}", stringService.countWords("hello world"));
        log.info("capitalize('codealpha')  = {}", stringService.capitalize("codealpha"));

        log.info("Application completed successfully.");
    }
}
