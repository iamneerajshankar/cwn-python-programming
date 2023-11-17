""" 
Python program to calculate time and space complexity of the different arrays
"""

class UnorderedArrayPair:

    """
    Function to calculate Time Complexity and Space Complexity of Two different Arrays
    """
    def print_undordered_pair(self, arr_a, arr_b): # Time Complexity --> O(n*m)
        for i in range(len(arr_a)): # -------------------------------------------->O(n)
            for j in range(len(arr_b)): # ----------------------------------------->O(m)
                if arr_a[i] < arr_b[j]: # ----------------------------------------->O(1)
                    print(str(arr_a[i]) + " is smaller than " + str(arr_b[j])) # --->O(1)