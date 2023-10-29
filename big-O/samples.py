# O(1) - Constant Time Complexity
def access_first_element(my_list):
    # This function returns the first element of the list.
    return my_list[0]

# O(c) - Constant Time Complexity
def add(a, b):
    # This function adds two numbers and returns the result.
    return a + b

# O(2N) - Linear Time Complexity
def linear_sum(numbers):
    # This function calculates the sum of a list of numbers using a loop.
    total = 0
    for num in numbers:
        total += num
    return total

# O(N^2) - Quadratic Time Complexity
def bubble_sort(arr):
    # This function sorts a list using the bubble sort algorithm.
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# O(log N) - Logarithmic Time Complexity
def binary_search(arr, target):
    # This function performs binary search to find the target element in a sorted list.
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# O(1) - Constant Space Complexity
def constant_space():
    # This function uses constant memory space.
    return 42

# O(N) - Linear Space Complexity
def linear_space(numbers):
    # This function creates a list that grows linearly with the input size.
    result = []
    for num in numbers:
        result.append(num)
    return result

# O(N^2) - Quadratic Space Complexity
def quadratic_space(N):
    # This function creates a 2D array of size N×N.
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    return matrix
