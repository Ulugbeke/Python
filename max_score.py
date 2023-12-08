student_scores = [65, 54, 12, 75, 33, 24, 654, 98, 17, 6, 1, 67, 34, 23]

highest_score = 0
for student_score in student_scores:
    if student_score > highest_score:
        highest_score=student_score

print(f'The highest score in the class is {highest_score}')
