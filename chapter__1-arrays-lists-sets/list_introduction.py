"""
Demonstration of List in Python and various Operations, Functions
"""
pretty_format = """
=================================================================================================================================
"""

class ListAsDataStructure():

    def create_and_traverse():
        """
        Function to show the list create and traverse using naive approach
        """
        season_fruits = ['mango', 'watermelon', 'black grapes', 'orange']
        print('The best fruits this season are: ', end=' ')
        for item in season_fruits:
            print(item, end=', ')
        print('\n')

        # Accessing the given elements
        mango = season_fruits[0]
        print(f"The first fruit in the list --> {mango}")
    
    def create_and_traverse_2d_list():
        """
        
        """
        natural_numbers = [[1, 2], [3, 4], [5, 6], [7, 8]]

        # Access the first item
        print(natural_numbers[0])


"""
Class Objects and Function calls
"""
if __name__ == '__main__':
    instance = ListAsDataStructure
    print(pretty_format)
    instance.create_and_traverse()
    print(pretty_format)
    instance.create_and_traverse_2d_list()
