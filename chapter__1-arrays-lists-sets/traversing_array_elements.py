"""
Python to program to demonstrate the array traversal
Time Complexity --> O(n)
Space Complexity --> O(1)
"""

from array import array as arr

def array_traversal(arr):
    print("The array elements are as follows: ", end="\t")
    for i in range(0, len(arr), 1):
        print(arr[i], end="\t")
    print("\n")

def array_traversal_2(arr):
    """
    Using range funtion to traverse through all array elements
    """
    print(f"The Traversal for array in begin to end: ", end="\t")
    for element in arr:
        print(element, end="\t")
    print("\n")


def traversing_array_reverse(arr):
    """
    Array Traversal in reverse order
    """
    print(f"The Traversal for array in end to beginning: ", end="\t")
    for i in range(len(arr)-1, -1, -1):
        print(arr[i], end="\t")
    print("\n")

if __name__ == "__main__":
    my_arr = arr('i', [2, 4, 5, 7, 1])

    # Making call to array_traversal function 
    array_traversal(my_arr)
    array_traversal_2(my_arr)
    traversing_array_reverse(my_arr)