# Andre McDonald
# 04/20/# Andre McDonald
# 04/20/2025
# P5LAB1
# A program to calculate the change owed to a customer

import random


def disperse_change(amount):
    # Convert amount to an integer number of cents
    cents = int(round(amount * 100))  # rounding helps with floating point issues

    # Define denominations in cents
    denominations = [
        (100, 'dollar', 'dollars'),
        (25, 'quarter', 'quarters'),
        (10, 'dime', 'dimes'),
        (5, 'nickel', 'nickels'),
        (1, 'penny', 'pennies'),
    ]

    # Calculate and display the number of each denomination
    for value, singular, plural in denominations:
        count = cents // value
        cents %= value  # reduce the remaining cents
        if count > 0:
            name = singular if count == 1 else plural
            print(f"{count} {name}")

def main():
    total_owed = round(random.uniform(0.01, 100.00), 2)  # Random amount between $0.01 and $100.00
    print(f"Total owed: ${total_owed:.2f}")
    # Prompt user to enter money

    amount = float(input("Enter the amount of money you have: $"))
    if amount < total_owed:
        print("Insufficent funds.")
    elif amount == total_owed:
        print("Exact amount. No change needed.")
    else:
        change = amount - total_owed
        print(f"Change owed: ${change:.2f}")
        print("Change to be returned:")
        # Call the function to disperse change
        disperse_change(change)       
        return


if __name__ == "__main__":
    main()