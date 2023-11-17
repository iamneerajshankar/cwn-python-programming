"""
Python program to insert a given element to the existing array
"""
from array import array as arr

def show_array(my_arr):
    print(f"The array elements are as follows: ")
    for element in my_arr:
        print(element, end="\t")
    print('\n')

def insert_at_start(my_arr, element):
    show_array(my_arr)
    for i in range(len(my_arr)-1, -1, -1):
        my_arr[i+1] = my_arr[i]
    my_arr[0] = element
    show_array(my_arr)


def insert_at_index(my_arr, index, element):
    """
    Insert Array element at given location
    """
    show_array(my_arr)
    for i in range(len(my_arr)-1, index-1, -1):
        my_arr[i+1] = my_arr[i]
    my_arr[index] = element
    show_array(my_arr)

"""
Function Calls
"""
my_arr = arr('i', [1, 2, 3, 4])
element = 5
# insert_at_start(my_arr, element)
insert_at_index(my_arr, 3, 10)

    
        


