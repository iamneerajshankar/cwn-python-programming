""" 
Given a list, write a function to get first, second best scores from the list.
"""

class BestScore:

    """ 
    function to show first and second best score
    """
    def best_score(self, my_list):
        my_list.sort(reverse=True)
        print(my_list)
        return myList[0], myList[1]
        


""" 
Create Object and Function Calls
"""
myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]

sol = BestScore()
result = sol.best_score(myList)
print(result)
print(type(result))