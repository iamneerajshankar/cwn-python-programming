""" 
-----------------------------------------------------------------------------------------------------------------------

"""


class UnderstandingListComprehension:
    animal_list = ["Jaguar", "Humans", "Jellyfish", "Beetles"]
    phylum_list = ["Chordata", "Chordata", "Cnidaria", "Arthropod"]

    @staticmethod
    def digit_sum(marks):
        total_sum = 0
        for item in marks:
            total_sum += item
        print(f"Total Sum: {total_sum}")

    # finding sum of grades using list comprehension
    @staticmethod
    def find_sum_of_digits(marks):
        total_marks = [(mark+mark) for mark in marks]
        print(f"Total Marks: {total_marks}")

    # ============ Coverts two list into list of two tuples =============================================
    def convert_to_list_to_tuples(self):
        animal_phylum_list = [
            (animal, phylum)
            for animal, phylum in zip(self.animal_list, self.phylum_list)
        ]
        return animal_phylum_list

    def reverse_each_string(self):
        reversed_animal_string_list = [
            new_string[::-1] for new_string in self.animal_list
        ]
        return reversed_animal_string_list



if __name__ == "__main__":

    grades = [7.65, 8.90, 4.50, 2.94]

    UnderstandingListComprehension().digit_sum(grades)
    UnderstandingListComprehension().find_sum_of_digits(grades)
