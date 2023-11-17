"""
Python program to demonstrate creation of array of different datatypes
"""
from array import array as arr
def create_int_arr():
    int_arr = arr("i", [1, 2, 3, 4, 5, 6])
    print(int_arr)

def create_double_arr():
    double_arr = arr("d", [1.30, 1.40, 3.30, 4.56])
    print(double_arr)

def get_array_attributes():
    print(arr.typecodes)

"""
Function calls
"""
if __name__ == "__main__":
    create_int_arr()
    create_double_arr()
    get_array_attributes()