# Task 3: Java Application using Gradle

## Overview
A **Java 17** application built and managed entirely with **Gradle**, demonstrating automated builds, dependency management, unit testing with JUnit 5, JaCoCo code coverage, and CI/CD via GitHub Actions.

## Project Structure
```
Task3-Java-Gradle/
├── build.gradle                    # Build config: plugins, deps, JaCoCo, fat-JAR task
├── settings.gradle                 # Project name
├── gradlew                         # Gradle wrapper
├── gradle/wrapper/
│   └── gradle-wrapper.properties   # Gradle 8.7 distribution
├── src/main/java/tech/codealpha/
│   ├── App.java                    # Main entry point
│   ├── MathService.java            # Math operations (6 methods)
│   └── StringService.java          # String operations (5 methods)
├── src/test/java/tech/codealpha/
│   ├── MathServiceTest.java        # 18 JUnit 5 tests
│   └── StringServiceTest.java      # 15 JUnit 5 tests
└── .github/workflows/gradle-ci.yml # CI matrix: Java 17 + 21
```

## Running the App

```bash
cd Task3-Java-Gradle

# Build (compiles + fat-JAR)
./gradlew build

# Run application
./gradlew run

# Run tests with coverage report
./gradlew test jacocoTestReport

# Check coverage ≥ 70%
./gradlew jacocoTestCoverageVerification

# Show dependency tree
./gradlew showDeps

# Run fat JAR directly
java -jar build/libs/codealpha-java-app-1.0.0-all.jar
```

## Dependencies

| Dependency | Version | Purpose |
|------------|---------|----------|
| JUnit 5 BOM | 5.10.2 | Unit testing |
| JUnit Jupiter | 5.10.2 | Test engine |
| SLF4J | 2.0.13 | Logging API |
| Logback | 1.5.6 | Logging implementation |

## Criteria Met
- ✅ Automated Java builds using Gradle (build, test, fatJar, showDeps tasks)
- ✅ Efficient dependency management (Maven Central, BOM)
- ✅ CI/CD via GitHub Actions (matrix: Java 17 + 21)
- ✅ Streamlined build & deployment (fat JAR, Gradle wrapper)
- ✅ DevOps principles: code coverage (JaCoCo 70%), style (Checkstyle)
