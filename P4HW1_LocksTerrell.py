# CTI-110
# P4HW1 - Score List
# Terrell Locks
# November 20, 2023
#

#asks user to enter number of scores, and create a list

scores_entered=int(input('How many scores do you want to enter? '))
i = 1
score_list=[]

print()

#create a loop

for i in range(scores_entered):
    i +=1
    final_score = float(input(f'Enter score #{i} : '))
    if final_score >= 0 and final_score <= 100:
        score_list.append(final_score)
    else:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        final_score = float(input(f'Enter score #{i} again: '))
        score_list.append(final_score)

        
low = min(score_list)
avg = sum(score_list) / 5

#create a value of the lowest score, and the average from the list 


if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
else:
    grade = 'F'

print()
print()

#program displays lowest score, modified list, average of list and grade, afterb deleting lowest score

print('-------------Results-----------')
print('Lowest Score  :',low)
score_list.remove(low)
avg = sum(score_list) / 4
print('Modified List :',score_list)
print('Scores Average:',f'{avg}')
print('Grade         :',grade)
print('---------------------------------')



