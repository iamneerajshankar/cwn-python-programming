""" 
Python program to form and print pairs of array elements

"""

def print_pairs(my_arr):
    """ 
    Time Complexity -----------> O(n2)
    Space Complexity ------------> 0(1)
    """
    for i in my_arr: # --------------------------------------->O(n)
        for j in my_arr: # --------------------------------------->O(n)
            print(str(i) + ", " + str(j)) # --------------------------------------->O(1)


""" 
"""
my_arr = [1, 2, 3, 4, 5, 6]
print_pairs(my_arr=my_arr)