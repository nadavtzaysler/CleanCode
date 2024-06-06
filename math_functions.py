import math

def calculate_triangular_number(num: int) -> int:
    if num <= 0:
        return 0
    return sum(range(num + 1))

def is_prime(num):
    if num <= 1:
        return False
    for divisor in range(2, int(math.sqrt(num)) + 1):
        if num % divisor == 0:
            return False
    return True

def factorial(num: int) -> int:
    if num < 0:
        raise ValueError("Negative values are not supported.")
    elif num == 0:
        return 1
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

def recursive_factorial(num: int) -> int:
    if num < 0:
        raise ValueError("Negative values are not supported.")
    elif num == 0 or num == 1:
        return 1
    else:
        return num * recursive_factorial(num-1)

def print_numbers(num: int) -> None:
    for i in range(num):
        if is_prime(i):
            print(f"{i} is prime")
        else:
            print(f"{i} is not prime")

def calculate_power(base: int, exponent: int) -> int:
    if exponent < 0:
        raise ValueError("Exponent cannot be negative.")
    elif exponent == 0:
        return 1
    else:
        return base ** exponent

def calculate_square_root(base: int) -> float:
    if base < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    else:
        return math.sqrt(base)

def calculate_hypotenuse(a: float, b: float) -> float:
    if a < 0 or b < 0:
        raise ValueError("Both sides must be positive.")
    else:
        return math.hypot(a, b)

def calculate_fibonacci_by_index(index: int) -> int:
    if index < 0:
        raise ValueError("Negative values are not supported.")
    elif index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, index + 1):
            a, b = b, a + b
        return b
    
def calculate_factorial_sum(num: int) -> int:
    if num < 0:
        raise ValueError("Negative values are not supported.")
    else:
        return sum(factorial(i) for i in range(num + 1))

def calculate_exponential_sum(exponent: int, num: int) -> int | None:
    if num < 0:
        raise ValueError("Number of terms cannot be negative.")
    else:
        return sum(calculate_power(exponent, i) / factorial(i) for i in range(num + 1))