from math_functions import print_numbers, calculate_triangular_number, factorial, calculate_power, calculate_square_root, calculate_hypotenuse, calculate_fibonacci_by_index, calculate_factorial_sum, calculate_exponential_sum


def main():
    while(True):
        try:
            num = int(input("Enter a number: "))
        except ValueError as e:
            print("please insert positive number")
            continue
        break

    print(f"Sum of numbers from 0 to {num}: {calculate_triangular_number(num)}")
    print(f"Factorial of {num}: {factorial(num)}")
    print_numbers(num)
    print(f"2^3 = {calculate_power(2, 3)}")
    print(f"Square root of 16: {calculate_square_root(16)}")
    print(f"Hypotenuse of 3 and 4: {calculate_hypotenuse(3, 4)}")
    print(f"Fibonacci sequence up to 10: {calculate_fibonacci_by_index(10)}")
    print(f"Factorial sum up to 5: {calculate_factorial_sum(5)}")
    print(f"Exponential sum of 2 up to 5 terms: {calculate_exponential_sum(2, 5)}")

if __name__ == "__main__":
    main()