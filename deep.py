            # ABOUT PROGRAM
'''In deep.py, implement a program that prompts the user for the answer to the 
Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 
42 or (case-insensitively) forty-two or forty two. Otherwise output No.'''

användar_inpute = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
användar_input = användar_inpute.lower().rstrip().lstrip()

if användar_input == "42":
    print("yes")
elif användar_input == "forty-two":
    print("yes")
elif användar_input == "forty two":
    print("yes")
else:
    print("no")