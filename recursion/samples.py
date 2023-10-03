# Calculate the power of two using recursion
def calculate_power_of_two(n):
    if n == 0:
        return 1
    else:
        power = calculate_power_of_two(n - 1)
        return power * 2

print(calculate_power_of_two(3))

# Calculate factorial using recursion
def calculate_factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be a positive integer only!'
    if n in [0, 1]:
        return 1
    else:
        return n * calculate_factorial(n - 1)

# Calculate Fibonacci number using recursion
def calculate_fibonacci(n):
    assert n >= 0 and int(n) == n, 'Fibonacci number cannot be a negative number or a non-integer.'
    if n in [0, 1]:
        return n
    else:
        return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)

print(calculate_fibonacci(7))
