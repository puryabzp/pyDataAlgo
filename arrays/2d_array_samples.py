# Importing NumPy library
import numpy as np

# Creating a 2D array using lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing an element
element = matrix[1][2]
print(f"Accessed element: {element}")

# Traversing the 2D array
print("Traversing the 2D array:")
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()

# Searching for an element
def search_2d_array(arr, target):
    for i, row in enumerate(arr):
        if target in row:
            return i, row.index(target)
    return -1, -1

target_element = 5
index_i, index_j = search_2d_array(matrix, target_element)
print(f"Element {target_element} found at index ({index_i}, {index_j})")

# Deleting a row
del matrix[1]
print("2nd row deleted:", matrix)

# Deleting an element
matrix[0].pop(1)
print("Element at row 0, column 1 deleted:", matrix)

# Using NumPy to create a 2D array
np_matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Sum of rows and columns using NumPy
sum_rows = np.sum(np_matrix, axis=1)  # Sum of each row
sum_cols = np.sum(np_matrix, axis=0)  # Sum of each column
print("Sum of rows:", sum_rows)
print("Sum of columns:", sum_cols)

# Deleting a row using NumPy
new_matrix_row_deleted = np.delete(np_matrix, 1, axis=0)
print("Row deleted using NumPy:", new_matrix_row_deleted)

# Deleting a column using NumPy
new_matrix_col_deleted = np.delete(np_matrix, 1, axis=1)
print("Column deleted using NumPy:", new_matrix_col_deleted)
