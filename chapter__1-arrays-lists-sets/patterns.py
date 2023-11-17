"""
-------------------------------------------------------------------------------------------------------------
1. Inverted Pyramind
2. Left Sided Pyramid
3. Right sided Pyramid
4. Diamond
"""


class Pattern:
    @staticmethod
    def create_inverted_pyramid(n):
        for i in range(n):
            x = "* "
            x = x * (n - i)
            print(f"{x: ^10}")

    @staticmethod
    def create_left_sided_pyramid(n):
        for i in range(n):
            x = "* "
            x = x * i
            print(f"{x:<10}")

    @staticmethod
    def create_right_sided_pyramid(n):
        for i in range(n):
            x = "* "
            x = x * i
            print(f"{x:>10}")

    @staticmethod
    def create_upright_pyramid(n):
        for i in range(n):
            x = "* "
            x = x * i
            print(f"{x:^10}")

    @staticmethod
    def create_diamond(n):
        for i in range(n):
            x = "* "
            x = x * i
            print(f"{x:^10}")

        for i in range(n):
            x = "* "
            x = x * (n - i)
            print(f"{x: ^10}")


if __name__ == "__main__":
    n = 5
    Pattern().create_inverted_pyramid(n)
    Pattern().create_left_sided_pyramid(n)
    Pattern().create_right_sided_pyramid(n)
    Pattern().create_upright_pyramid(n)
    Pattern().create_diamond(n)
