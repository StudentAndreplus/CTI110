Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
module_grades = []

for i in range(1,7):
    
SyntaxError: multiple statements found while compiling a single statement

================================ RESTART: Shell ================================
# Create list to hold grades inside of
module_grades = []

#Take grades from user input and add them to the list
for i in range (1,7):
    grade = float(input(f"Enter the grade for module {i}: ")
    module_grades.appead(grade)
#Calculate the stats using list methods
lowest_grade = min(module_grades)# getting the smallest grade in the list
highest_grade = max(module_grades) # getting the larges grade in the list
sum_of_grades =  sum(module_grades)# getting the sum of all the grades
average_grade = sum_of_grades / len(module_grades) # getting the grade average by dividing the sum of the grades by the length of the list

#Display the results
                  
SyntaxError: multiple statements found while compiling a single statement
print(f"Lowest Grade:  {lowest_grade}")
print(f"Highest Grade:  {highest_grade}")
print(f"Sum of Grades:  {sum of_grades}")
print(f"Grade Average:  {average_grade}")
                  
SyntaxError: multiple statements found while compiling a single statement

================================ RESTART: Shell ================================
# Create list to hold grades inside of
module_grades = []

#Take grades from user input and add them to the list
for i in range (1,7):
    grade = float(input(f"Enter the grade for module {i}: "))
    module_grades.appead(grade)
                  
#Calculate the stats using list methods
lowest_grade = min(module_grades)# getting the smallest grade in the list
highest_grade = max(module_grades) # getting the larges grade in the list
sum_of_grades =  sum(module_grades)# getting the sum of all the grades
average_grade = sum_of_grades / len(module_grades) # getting the grade average by dividing the sum of the grades by the length of the list

#Display the results
                  

print(f"Lowest Grade:  {lowest_grade}")
print(f"Highest Grade:  {highest_grade}")
print(f"Sum of Grades:  {sum_of_grades}")
print(f"Grade Average:  {average_grade:.2f}")
                  
SyntaxError: multiple statements found while compiling a single statement

================================ RESTART: Shell ================================
# Create list to hold grades inside of
module_grades = []

#Take grades from user input and add them to the list
for i in range (1,7):
    grade = float(input(f"Enter the grade for module {i}: "))
    module_grades.appead(grade)
                  
#Calculate the stats using list methods
lowest_grade = min(module_grades)# getting the smallest grade in the list
highest_grade = max(module_grades) # getting the larges grade in the list
sum_of_grades =  sum(module_grades)# getting the sum of all the grades
average_grade = sum_of_grades / len(module_grades) # getting the grade average by dividing the sum of the grades by the length of the list

#Display the results
                  

print(f"Lowest Grade:  {lowest_grade}")
print(f"Highest Grade:  {highest_grade}")
print(f"Sum of Grades:  {sum_of_grades}")
print(f"Grade Average:  {average_grade:.2f}")
                  
SyntaxError: multiple statements found while compiling a single statement

= RESTART: /Users/andre-macbook/Desktop/Desktop - Andre’s MacBook Air/School Work/Web,Db, Pgm/P2HW/P2HW2.py
Enter the grade for module 1: 80
Enter the grade for module 2: 89
Enter the grade for module 3: 88
Enter the grade for module 4: 90
Enter the grade for module 5: 70
Enter the grade for module 6: 90
Lowest Grade:  70.0
Highest Grade:  90.0
Sum of Grades:  507.0
Grade Average:  84.50

= RESTART: /Users/andre-macbook/Desktop/Desktop - Andre’s MacBook Air/School Work/Web,Db, Pgm/P2HW/P2HW2.py
Enter the grade for module 1: 78
Enter the grade for module 2: 89
Enter the grade for module 3: 90
Enter the grade for module 4: 97
Enter the grade for module 5: 70
Enter the grade for module 6: 87
------ Result ------
Lowest Grade:  70.0
Highest Grade:  97.0
Sum of Grades:  511.0
Grade Average:  85.17

= RESTART: /Users/andre-macbook/Desktop/Desktop - Andre’s MacBook Air/School Work/Web,Db, Pgm/P1HW2/P1HW2_McDonaldAndre.py
Enter your budget: 6000
Enter your travel destination: Bali
Enter the amount you will spend on gas: 0
Enter the amount you will spend on accommodation: 500
Enter the amount you will spend on food: 200
Travel destination: Bali
Total expenses: $700.0
Remaining budget: $5300.0

= RESTART: /Users/andre-macbook/Desktop/Desktop - Andre’s MacBook Air/School Work/Web,Db, Pgm/P1HW2/P1HW2_McDonaldAndre.py
Enter your budget: 10000
Enter your travel destination: Bali
Enter the amount you will spend on gas: 120
Enter the amount you will spend on accommodation: 400
Enter the amount you will spend on food: 200
Travel destination: Bali
Total expenses:     $    720.00
Remaining budget:   $1.00

= RESTART: /Users/andre-macbook/Desktop/Desktop - Andre’s MacBook Air/School Work/Web,Db, Pgm/P1HW2/P1HW2_McDonaldAndre.py
Enter your budget: 8000
Enter your travel destination: Oakland
Enter the amount you will spend on gas: 50
Enter the amount you will spend on accommodation: 150
Enter the amount you will spend on food: 400
Travel destination: Oakland
Total expenses:     $    600.00
Remaining budget:   $1.00
>>> 
= RESTART: /Users/andre-macbook/Desktop/Desktop - Andre’s MacBook Air/School Work/Web,Db, Pgm/P1HW2/P1HW2_McDonaldAndre.py
Enter your budget: 8000
Enter your travel destination: Oakland
Enter the amount you will spend on gas: 50
Enter the amount you will spend on accommodation: 150
Enter the amount you will spend on food: 400
Travel destination: Oakland
Total expenses:     $    600.00
Traceback (most recent call last):
  File "/Users/andre-macbook/Desktop/Desktop - Andre’s MacBook Air/School Work/Web,Db, Pgm/P1HW2/P1HW2_McDonaldAndre.py", line 35, in <module>
    travel_budget()
  File "/Users/andre-macbook/Desktop/Desktop - Andre’s MacBook Air/School Work/Web,Db, Pgm/P1HW2/P1HW2_McDonaldAndre.py", line 32, in travel_budget
    print(f"{'Remaining budget:' :<20}${remaining_budget:>10:.2f}")
ValueError: Invalid format specifier '>10:.2f' for object of type 'float'
>>> 
= RESTART: /Users/andre-macbook/Desktop/Desktop - Andre’s MacBook Air/School Work/Web,Db, Pgm/P1HW2/P1HW2_McDonaldAndre.py
Enter your budget: 8000
Enter your travel destination: Oakland
Enter the amount you will spend on gas: 50
Enter the amount you will spend on accommodation: 150
Enter the amount you will spend on food: 400
Travel destination: Oakland
Total expenses:     $    600.00
Remaining budget:   $   7400.00
