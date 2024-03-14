'''
The program takes a list of integers, positive or negative, and returns the sum of the positive numbers in the list.

Usage:
    Input: 4, 1, 0, -5, 4, -1, -8, 0
    Output: The sum is 9
'''

import re

class Library(object):
    def get_digits(self, temp):
        ''' Prompts the user until the prompt is a list of numbers separated by commas and spaces.

            Arguments:
                temp: The prompt message given to the user

            Returns:
                An string digits, or None if the user doesn't provide a valid input. 
        '''
        while True:
            input_val = input(temp)

            if input_val.startswith("[") and input_val.endswith("]"):
                print("Invalid input. Please enter a list of numbers without square brackets.")
                continue
            
            pattern = re.compile(r"^[\+\-]?\d+(,\s[\+\-]?\d+)*$")
            if (pattern.search(input_val)) is not None:
                return input_val
            print("Invalid input. Please enter a list of numbers separated by commas and spaces.")

def main():
    library = Library() # Object of class library
    numbers = library.get_digits("Enter a list of numbers separated by commas and spaces: ")
    numbers_list = numbers.split(", ")
    Sum = 0
    for n in numbers_list:
        num = int(n)
        if int(num) > 0:
            Sum += num
    print(Sum)

if __name__ == "__main__":
    main()