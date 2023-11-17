"""
Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
"""

def middle_function(my_list):
    middle_list = my_list[1:len(my_list)-1]
    return middle_list



"""
"""
if __name__ == "__main__":

    arr = [1, 2, 3, 4]
    result = middle_function(arr)
    print(result)
