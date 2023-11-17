"""
=================================================================================================================================
Array Practice Problems in Python 
=================================================================================================================================
"""
from array import array

class PracticeProblems():

    def create_and_traverse(self, my_arr):
        print(f"The array element are as follows: ", end=" ")
        for element in my_arr:
            print(element, end=" ")

    def access_individual_element(self, my_arr):
        #access and print array at index 2
        print(f"The array at index 2 is: {my_arr[2]}")
    
    def append_value_to_arr(self, my_arr):
        my_arr.append(5)
        self.create_and_traverse(my_arr)
    
    def insert_value_in_arr(self, my_arr):
        index = 2
        element = 10
        my_arr.insert(2, 10)
        self.create_and_traverse(my_arr)
        


"""
=================================================================================================================================
Object creation and function calls
=================================================================================================================================
"""
format_string = """
=================================================================================================================================
"""


# Create an array of integers
arr = array('i', [1, 2, 3, 4])
practice_set = PracticeProblems()


practice_set.create_and_traverse(arr)
print(format_string)
#find array given location
practice_set.access_individual_element(arr)
print(format_string)
# append element to an array

practice_set.append_value_to_arr(arr)
print(format_string)

# insert and element to array at given index
practice_set.insert_value_in_arr(arr)
print(format_string)
