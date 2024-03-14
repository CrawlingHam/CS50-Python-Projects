'''
Why did i build this? At the time  i was in high school, and i was wondering how many weeks my vacations were,
and i also wanted to know how many weeks and days a year i have no school. i later used
this to also calculate how many free days i had when i started working to plan my vacations better

A lot of these projects are very useful for small day to day problems.
'''

class Library(object):

    def get_input(self, prompt):
        while True:
            try:
                input_val = input(prompt)
                int_val = int(input_val)
                if isinstance(int_val, int) and int_val > 0:
                    return int_val
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input. Please enter a number.")

library = Library()
vacation = library.get_input("Enter the number of vacation days: ")

week = vacation // 7
days = vacation % 7


if week < 1 and days == 1:
    print(f"{days} day of vacation.")
elif week < 1 and days > 1:
    print(f"{days} days of vacation.")
elif week > 1 and days < 1:
    print(f"{week} weeks of vacation.")
elif week == 1 and days == 1:
    print(f"{week} week and {days} day of vacation.")
elif week == 1 and days > 1:
    print(f"{week} week and {days} days of vacation.")
elif week > 1 and days == 1:
    print(f"{week} weeks and {days} day of vacation.")
elif week > 1 and days > 1:
    print(f"{week} weeks and {days} days of vacation.")
else:
    print("Failed to calculate number of days of vacation.")
