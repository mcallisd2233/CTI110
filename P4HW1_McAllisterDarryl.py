#CTI-110
#P4HW1 - Score List
#Darryl McAllister
#4/27/2023
#Ask user to enter a set number of scores then evaluates and removes lowest value, prints scores, and calculates the average.

scores_list = []

num_scores = int(input('How many scores do you want to enter? '))

for num in range(1, num_scores + 1):
    score = int(input(f'Enter score #{num}: '))
    scores_list.append(score)
    if score < 0 or score > 100:
        scores_list.pop(-1)
        print('INVALID Score entered!!')
        print('Score should be between 0 and 100')
        score = int(input(f'Enter score #{num} again: '))
        scores_list.append(score)
        
print('\n--------Results--------')
print('Lowest Score:', min(scores_list))
scores_list.remove(min(scores_list))
print('Modified List:', scores_list)
print('Scores Average:', sum(scores_list)/len(scores_list))
scores_avg = sum(scores_list)/len(scores_list)

if scores_avg >= 90:
    print('Grade: A')
elif scores_avg >= 80:
    print('Grade: B')
elif scores_avg >= 70:
    print('Grade: C')
elif scores_avg >= 60:
    print('Grade: D')
else:
    print('Grade: F')

print('----------------------')
