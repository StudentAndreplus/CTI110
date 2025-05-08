# Andre McDonald
# 04/18/2025    
# This program calculates the gallons of gas needed for a trip based on the car's MPG.
# P2LAB2
car_mpg = {'Camaro':18.21,'Prius':52.36,'Model S':110,'Silverado':26
}       

keys = car_mpg.keys()

print("Available Cars:")
for car in keys:
    print(car)

selected_car = input("\nEnter the name of the vehicle exactly as it's shown above: ")

if selected_car in car_mpg:
    mpg = car_mpg[selected_car]
    print(f"\nThe {selected_car} gets {mpg} miles per gallon.")

    miles = float(input("\nEnter the number of miles you plan to drive: "))

    gallons_needed = miles / mpg
    print(f"\nYou will need {gallons_needed:.2f} gallons of gas for {miles} miles.")
else:
    print("\nError: Vehicle not found.")