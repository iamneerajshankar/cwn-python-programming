""" 
Python program to find the find maximum of prodcut of any two numbers taken from given array
"""

import numpy as np

class FindMaxProduct:

    """ 
    Naive Approach --> returns the max product of possible of any two numbers in arr
    """
    def max_product(self, arr):
        maximum_product = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                pair_product = arr[i] * arr[j]
                if pair_product > maximum_product:
                    maximum_product = pair_product
                    pair = str(arr[i]) + ", " + str(arr[j])
        
        print(f"The pairs that gives max prodcut--> {pair}")
        print(f"The maximum product possible --> {maximum_product}")


""" 
Create of object and funcation calls
"""
my_arr = np.array([1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 16, 27, 58, 19, 21])
find_max = FindMaxProduct()
find_max.max_product(my_arr)
    
