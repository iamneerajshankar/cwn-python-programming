"""
Create an 2-D Array using the numpy
"""

import numpy as np

class TwoDimentionalArray():

    def print_array(self, arr):
        print('========================================================================================================')
        print(f"The output is as follows: ")
        print(arr)

    def create_2d_array(self):
        two_dimensional_array = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 19]])
        return two_dimensional_array
    

    def accessing_element(self):
        
        arr = self.create_2d_array()
        second_row_first_element = arr[1][0]
        return second_row_first_element
    
    def traversing_through_array(self):
        arr = self.create_2d_array()
        try:
            print("Traversing a 2-d array: ")
            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    print(arr[i][j], end=" ")
            print("\n")
        except IndexError:
            print("Index out of scope.")
        
    def insert_element_into_array(self):
        arr = self.create_2d_array()
        # Inserting row or column to a 2-d array
        new_col1 = [1, 2, 3, 4]
        new_2d_array = np.insert(arr, 0, new_col1, axis=1)

        new_row1 = [5, 6, 7, 9]
        new_2d_array = np.insert(arr, 1, new_row1, axis=0)
        
        return arr
    

"""
Creating objects and calling the functions
"""

if __name__ == '__main__':
    instance = TwoDimentionalArray()

    
        


