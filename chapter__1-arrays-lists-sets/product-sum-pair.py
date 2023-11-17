""" 
Python program to calculate the sum and product of elements in given list or array
"""

class ProductSumPairMethods:

    """ 
    Function to find out and return product and sum pair
    """
    def product_sum_pair(self, my_list):
        sum = 0 # --------------------------------------->O(1)
        product = 1 # --------------------------------------->O(1)
        for i in range(len(my_list)): # --------------------------------------->O(n)
            sum += my_list[i] # --------------------------------------->O(1)
        for j in range(len(my_list)): # --------------------------------------->O(n)
            product += my_list[j] # --------------------------------------->O(1)
        
        return sum, product 


""" 
Object creation and function calls
"""

my_list = [1, 2, 3, 4, 5, 6, 7]
sol = ProductSumPairMethods()
result = sol.product_sum_pair(my_list)
print(result)