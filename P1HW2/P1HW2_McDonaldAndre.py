# Andre McDonald
# 04/20/2025
# P2HW2
# a program that does some basic math on numbers that are entered

# Start of program

    # Step 1: Ask user to enter their budget
budget = float(input("Enter your budget: "))

    # Step 2: Ask user to enter travel destination
destination = input("Enter your travel destination: ")

    # Step 3: Ask user for amount they will spend on gas
gas_expense = float(input("Enter the amount you will spend on gas: "))

    # Step 4: Ask user for amount they will spend on accommodation
accommodation_expense = float(input("Enter the amount you will spend on accommodation: "))

    # Step 5: Ask user for amount they will spend on food
food_expense = float(input("Enter the amount you will spend on food: "))

    # Step 6: Add expenses
total_expenses = gas_expense + accommodation_expense + food_expense

    # Step 6: Subtract expenses from budget
remaining_budget = budget - total_expenses

    # Step 7: Display results
print(f"{'Travel destination:' :<20}{destination}")
print(f"{'Total expenses:' :<20}${total_expenses:>10.2f}")
print(f"{'Remaining budget:' :<20}${remaining_budget:>10.2f}")

# Call the function to run the program

