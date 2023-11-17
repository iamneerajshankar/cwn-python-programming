""" 
Find pairs of element whose sum is excactly equal to given target element
"""

class SumPairs:

    """ 
    function to find the pair of elements whose sum matches the target number
    """
    def sum_pairs(self, arr, target):
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == arr[j]:
                    continue
                elif arr[i] + arr[j] == target:
                    print(arr[i], arr[j])
                

""" 
Create Object and Function calls
"""

arr = [1, 2, 3, 2, 3, 4, 5, 6]
target = 6
solution = SumPairs()
solution.sum_pairs(arr, target)