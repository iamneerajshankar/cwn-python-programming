""" 
Find the missing number from list of 1 to 100 numbers
"""


class MissingNumber:
    """ 
    Naive Approach to solve the problem of finding missing numbers
    """
    def find_missing_number(self, arr):
        missing_numbers = []
        for i in range(1, len(arr)-1, 1):
            diff = arr[i +1] - arr[i]
            if diff > 1:
                missing_numbers.append(arr[i]+ (diff -1))
        
        return missing_numbers
    
    """ 
    function to find the missing number from 1 to 100
    """
    def find_missing_number_2(self, arr, n):
        # sum of 1 to n natural numbers
        sum1 = n*(n+1)/2
        # sum of the numbers in the list/arr
        sum2 = sum(arr)
        return sum1 - sum2



""" 
"""
my_arr = []
for i in range(1, 101, 1):
    my_arr.append(i)

my_arr.remove(66)

solution = MissingNumber()
result = solution.find_missing_number(my_arr)
print(f"The missing numbers from list as follow: {result}")

result2 = solution.find_missing_number_2(my_arr, 100)
print(f"The missing Number from 1 to 100: {result2}")