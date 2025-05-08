# Andre McDonald
# Web, Pgm, & Db Foundation (CTI-110-0902)
# P4LAB2
# 04/12/25


reset = "yes"

while reset.lower() == "yes":
    try:
        number = int(input('enter a number: '))
        if number >= 0:
            print(f"\nMultiplication tablbe for {number}:")
            for i in range(1,13):
                print(f"{number} x {i} = {number * i}")
        else:
            print("Sorry, I cannot accept negative values.")
    except ValueError:
        print("That wasn't a valid integer. please enter an integer")

    reset = input("Do you want to run the program again? (yes or no) ")     

print("Closing Program...") 