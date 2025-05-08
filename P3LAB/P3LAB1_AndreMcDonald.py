# Andre McDonald
# 04/20/# Andre McDonald
# 04/20/2025
# P3LAB1
# A program to calculate the most efficient number of dollars, quarters, dimes, nickels, and pennies needed to make the given amount of money.

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
# Prompt user to enter money
amount = float(input("Enter the amount of money you have: $"))
disperse_change(amount)
