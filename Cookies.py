
'''
The program reads in two pieces of information from the user: the number of cookies and the number of people.
Then the program calculates how many cookies each person gets and how many cookies are left over. 
No cookies can be shared, but the number of cookies per child and the number of cookies left over must be whole numbers. 
The program should print out how many cookies each child gets. If there are cookies left, the program should also print the number of cookies remaining.
Depending on whether there are one or more cookies left, "cake" or "cookies" should be printed.

Usage:
    Input:
        Number of cookies: 17
        Number of people: 4
    Output:
        Cookies per person: 4
        1 cookie left over
'''
import sys
sys.path.append("..") 
from Reusable_code.Must_contain import must_contain_this # Import the class

def get_valid_input():
    must_contain = must_contain_this()
    while True:
        number_of_people = input("Number of cookies: ")
        if not must_contain.must_contain_digit(number_of_people): # Validate input
            print("Invalid input. Please enter a positive number.")
            continue # Restart the loop immediately

        number_of_cookies = input("Number of people: ")
        if not must_contain.must_contain_digit(number_of_cookies): 
            print("Invalid input. Please enter a positive number.")
            continue 

        return int(number_of_people), int(number_of_cookies)

def cookies():
    people, cookies = get_valid_input() # Get user input
    cookies_per_person = people // cookies
    leftover_cookies = people % cookies  # Leftover cookies
    if leftover_cookies > 1 and cookies_per_person > 1: # If both are bigger than 1 
        print(f"{cookies_per_person} cookies per person")
        print(f"{leftover_cookies} cookies left over.")
    elif leftover_cookies == 1 and cookies_per_person == 1: # If both are equal to 1 
        print(f"{cookies_per_person} cookie per person")
        print(f"{leftover_cookies} cookie left over.")
    elif leftover_cookies > 1 and cookies_per_person == 1: # If more than 1 cookie is left over 
        print(f"{cookies_per_person} cookie per person")
        print(f"{leftover_cookies} cookies left over.")
    elif leftover_cookies == 1 and cookies_per_person > 1: # If one of them is equal to one
        print(f"{cookies_per_person} cookies per person")
        print(f"{leftover_cookies} cookie left over.")
    elif leftover_cookies < 1 and cookies_per_person >= 1:
        print(f"{cookies_per_person} cookies per person")
    else:
        print("Error. Please try again")

if __name__ == '__main__':
    cookies()