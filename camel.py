# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> How the program works <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# i = index of the current character
# char = current character
# for loop is iterating through the string, storing the current char and its index
# if statement is checking if the current character is uppercase AND its index is not the first letter
# in which case => wherever the index is, '_' is added before the current character, then the current character is turned lowercase
# if first letter is uppercase => lower the first letter end loop
# print out the snake case

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> simple <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


user_input = str(input("camelCase: "))
snake_case = ''

for i, char in enumerate(user_input):
    if char.isupper() and i != 0:
        snake_case = snake_case + '_' + char.lower()
    else:
        snake_case = snake_case + char.lower()

print(f"snake_case: {snake_case}")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Object oriented <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def snake_caser(user_input):
    snake_case = ''

    for i, char in enumerate(user_input):
        if char.isupper() and i != 0:
            snake_case += '_' + char.lower()
        else:
            snake_case += char.lower()
    return snake_case

def main():
    user_input = str(input("camelcase: "))
    snake_cased = snake_caser(user_input)
    print(f"snakecase: {snake_cased}")


if __name__ == '__main__':
    main()