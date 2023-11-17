""" 
Given 2D list calculate the sum of diagonal elements.
"""

class DiagonalSum:

    """ 
    function to calculate the sum of diagonal elements
    """
    def diagonal_sum(self, my_list_2d):
        total = 0
        for i in range(len(my_list_2d)):
            for j in range(len(my_list_2d)):
                if i == j:
                    total += my_list_2d[i][j]

        return total
    
    """ 
    Efficient way
    """
    def diagonal_sum2(self, my_list_2d):
        sum = 0
        for i in range(len(my_list_2d)):
            sum += my_list_2d[i][i]

        return sum    


""" 
""" 
myList2D= [[1,2,3],[4,5,6],[7,8,9]] 

sol = DiagonalSum()
result = sol.diagonal_sum(myList2D)
print(result)

result = sol.diagonal_sum2(myList2D)
print(result)