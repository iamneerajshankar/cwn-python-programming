"""


"""


class CaesarCipher:

    @staticmethod
    def naive_caesar_cipher(s, k):
        ciphered_list = []
        letter_ascii_start_point = 65
        letter_ascii_stop_point = 90

        for c in s:
            if ord(c) in range(letter_ascii_start_point, letter_ascii_stop_point+1-k) or ord(c) in range():
                equivalent_ascii_number = ord(c) + k
                print(f"equivalent ascii number in if-condition -->{equivalent_ascii_number}")

            else:
                effective_incremental_point = ord(c) + k - letter_ascii_stop_point
                equivalent_ascii_number = letter_ascii_start_point + effective_incremental_point
                print(f"equivalent ascii number in else-condition -->{equivalent_ascii_number}")

            print(f"The equivalent Ascii number --> {equivalent_ascii_number}")
            if c.isalpha():
                ciphered_list.append(chr(equivalent_ascii_number))
            else:
                ciphered_list.append(c)

        print(f"ciphered list --> {ciphered_list}")
        return s

    @staticmethod
    def caesar_cipher_encrypt(s, k):
        encrypted_message = ''
        print(f"The rotating factor --> {k}")
        for char in s:
            print(f"The fetched character --> {char}")
            if char.isalpha():
                if char.islower():
                    equivalent_ascii_number = ord("a")
                else:
                    equivalent_ascii_number = ord("A")

                shifted_position = (ord(char) - equivalent_ascii_number + k) % 26
                encrypted_char = chr(equivalent_ascii_number + shifted_position)
                print(f"The character ascii value --> {equivalent_ascii_number + shifted_position}")
                encrypted_message += encrypted_char
            else:
                encrypted_message += char

        return encrypted_message


"""
"""
fptr = open('output_file.txt', 'w')

n = int(input().strip())

in_string = input()

rotating_factor = int(input().strip())

result = CaesarCipher.caesar_cipher_encrypt(in_string, rotating_factor)

fptr.write(result + '\n')

fptr.close()
