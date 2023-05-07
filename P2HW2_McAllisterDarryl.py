#CTI-110
#P2HW2 - List
#Darryl McAllister
#4/28/2023
#Ask user to enter six grades then evalutes lowest grade, highest grade, sum of grades, and grades average.

grade_list = []

for num in range(1, 7):
    grade = float(input(f'Enter grade for Module {num}: '))
    grade_list.append(grade)
    
print('\n--------Results--------')
print('Lowest Grade:', min(grade_list))
print('Highest Grade:', max(grade_list))
print('Sum of Grades:', sum(grade_list))
print('Average:', sum(grade_list)/len(grade_list))

print('----------------------')

