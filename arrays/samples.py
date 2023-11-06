# Import the 'array' class from the 'array' module
from array import array

# Create an array of signed integers ('i') and initialize it with values
# The 'i' type code represents signed integers
# The array will contain the elements: 1, 2, 3, 4, and 5
arr = array('i', [1, 2, 3, 4, 5])


# Insertion (Append)
arr.append(6)  # Appending element 6 to the end

# Deletion (Pop)
last_element = arr.pop()  # Removing and getting the last element

# Traversing (Iterating)
for element in arr:
    print(f"Element: {element}")

# Accessing (By Index)
third_element = arr[2]  # Accessing the element at index 2 (3)

# Searching
value_to_find = 4
if value_to_find in arr:
    index = arr.index(value_to_find)
    print(f"{value_to_find} found at index {index}")

# Deletion (Remove by Value)
value_to_remove = 3
if value_to_remove in arr:
    arr.remove(value_to_remove)  # Removing value 3

# Array Methods in Python

# extend()
arr1 = array("i",[1, 2, 3])
arr2 = array("i",[4, 5, 6])
arr1.extend(arr2)  # Appends elements from arr2 to arr1


# index()
index = arr1.index(4)  # Returns the index of value 4

# reverse()
arr1.reverse()  # Reverses the order of elements

# buffer_info()
buffer_info = arr1.buffer_info()  # Returns address and size of the array's buffer

# Printing results
print("Updated Array:", arr)
print("Removed Element:", last_element)
print("Third Element:", third_element)
print("Index of 4:", index)
print("Array after reversing:", arr1)
print("Buffer Info:", buffer_info)



