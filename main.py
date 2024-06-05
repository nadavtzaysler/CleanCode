import math

def calculate_sum(num: int) -> int:
    if num <= 0:
        return 0
    return sum(range(num))

def is_prime(num: int) -> bool:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return num > 2

def factorial(num: int) -> int | None:
    if num < 0:
        raise ValueError("Negative values are not supported.")
    elif num == 0:
        return 1
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

def recursive_factorial(num: int) -> int | None:
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

def calculate_power(base: int, exponent: int) -> int | None:
    if exponent < 0:
        raise ValueError("Exponent cannot be negative.")
    elif exponent == 0:
        return 1
    else:
        return base ** exponent

def calculate_square_root(base: int) -> int | float | None:
    if base < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    else:
        return math.sqrt(base)

def calculate_hypotenuse(a: int, b: int) -> int | None:
    if a < 0 or b < 0:
        raise ValueError("Both sides must be positive.")
    else:
        return math.hypot(a, b)

def calculate_fibonacci(num: int) -> int | None:
    if num < 0:
        raise ValueError("Negative values are not supported.")
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, num + 1):
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

def main():
    try:
        num = int(input("Enter a number: "))
        print(f"Sum of numbers from 0 to {num}: {calculate_sum(num)}")
        print(f"Factorial of {num}: {factorial(num)}")
        print_numbers(num)
        print(f"2^3 = {calculate_power(2, 3)}")
        print(f"Square root of 16: {calculate_square_root(16)}")
        print(f"Hypotenuse of 3 and 4: {calculate_hypotenuse(3, 4)}")
        print(f"Fibonacci sequence up to 10: {calculate_fibonacci(10)}")
        print(f"Factorial sum up to 5: {calculate_factorial_sum(5)}")
        print(f"Exponential sum of 2 up to 5 terms: {calculate_exponential_sum(2, 5)}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()