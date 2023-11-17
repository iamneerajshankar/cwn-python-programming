

class ListPracticeQuestions():

    def question_one(self):
        data = [[1, 2], [3, 4], [5, 6], [7, 8]]
        accessed_element = data[0][0]

        for row in data:
            for element in row:
                if accessed_element < element:
                    accessed_element = element
            
        return accessed_element
        


"""

"""
instance = ListPracticeQuestions()
result = instance.question_one()
print(result)