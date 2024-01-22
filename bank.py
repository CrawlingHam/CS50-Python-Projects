            # ABOUT PROGRAM
'''In a file called bank.py, implement a program that prompts the user for a greeting. 
If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), 
output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.'''

greeting = str(input("Greeting: " ))

edited = greeting.lstrip().rstrip().lower()
word = edited.split()[0]

if word == "hello":
    print("$0")
elif word[0] == "h" and word != "hello":
    print("$20")
else:
    print("$100")