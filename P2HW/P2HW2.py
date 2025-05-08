 #Andre McDonald

 #D04/20/2025

 #P2HW2

 #a program to take module grades and store them in a list to display 



module_grades = []

#Take grades from user input and add them to the list
for i in range (1,7):
    grade = float(input(f"Enter the grade for module {i}: "))
    module_grades.append(grade)
                  
#Calculate the stats using list methods
lowest_grade = min(module_grades)# getting the smallest grade in the list
highest_grade = max(module_grades) # getting the larges grade in the list
sum_of_grades =  sum(module_grades)# getting the sum of all the grades
average_grade = sum_of_grades / len(module_grades) # getting the grade average by dividing the sum of the grades by the length of the list

#Display the results
                  
print(f"------ Result ------")
print(f"Lowest Grade:  {lowest_grade}")
print(f"Highest Grade:  {highest_grade}")
print(f"Sum of Grades:  {sum_of_grades}")
print(f"Grade Average:  {average_grade:.2f}")

                  

