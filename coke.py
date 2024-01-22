# >>>>>>>>>>>>>>>>>>>>>>>>>>>> How the program will work <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 50 coins will be inserted
# while the amount of coins to insert is greater than 0:
# print the due amount first, then prompt user for amount of coins to insert
# ignores coins that are not 5, 10, 25, or 50. inserted amount of coins must be 5, 10, 25, or 50
# when amount of coins due == 0: print amount of change owed. Ex: change owed: 0 or change owed: 50


amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")

    coin_input = int(input("Insert coin: "))

    if coin_input in [5, 10, 25,50]:
        amount_due -= coin_input

change_owed = abs(amount_due)
print(f"Change Owed: {change_owed}")