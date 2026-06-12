"""Simple calculator module – used to demonstrate Jenkins remoting builds."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


def power(base: float, exp: float) -> float:
    return base ** exp


def modulo(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Modulo by zero is not allowed")
    return a % b
