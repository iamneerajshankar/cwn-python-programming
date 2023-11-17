"""
-----------------------------------------------------------------------------------------------------------------------
You are given a string containing characters A and B only. Your task is to change it into a string such that there are no 
matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.

"""

class AlternatingString:

    def __init__(self, s):
        self.in_string = s

    
    def using_naive_approach(self):

        deletion_count = 0
        alernate_string_list = []
        prev_chr =self.in_string[0]
        for i in range (1, len(self.in_string)):
            if prev_chr == self.in_string[i]:
                deletion_count += 1
            else:
                alernate_string_list.append(prev_chr)
                prev_chr = self.in_string[i]
        print(f"The New List: {alernate_string_list}")
        print(F"Deletion Required: {deletion_count}")

        return deletion_count


if __name__ == "__main__":

    input_string = "AAABBB"
    AlternatingString(input_string).using_naive_approach()