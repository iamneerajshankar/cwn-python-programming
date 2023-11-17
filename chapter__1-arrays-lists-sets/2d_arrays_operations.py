"""
Create an 2-D Array using the numpy
"""

import numpy as np

two_dimensional_array = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 19]])
print(f'Here is the 2-D array created: {two_dimensional_array}')

# Accessing element of 2-d array
second_row_first_element = two_dimensional_array[1][0]
print(f'Here is the first element of the second row: {second_row_first_element}')

# Traversing a 2-d array
try:
    print("Traversing a 2-d array: ")
    for i in range(len(two_dimensional_array)):
        for j in range(len(two_dimensional_array[0])):
            print(two_dimensional_array[i][j], end=" ")
        print("\n")
except IndexError:
    print("Index out of scope.")

# Inserting row or column to a 2-d array
new_col1 = [1, 2, 3, 4]
new_2d_array = np.insert(two_dimensional_array, 0, new_col1, axis=1)
print(f'Below is the two dimensional array: ')
print(new_2d_array)

new_row1 = [5, 6, 7, 9]
new_2d_array = np.insert(two_dimensional_array, 1, new_row1, axis=0)
print(f'Below is the new array with new row inserted: ')
print(new_2d_array)
