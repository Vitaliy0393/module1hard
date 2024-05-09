grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
#print(students)

sum_grades = sum(grades[0]),sum(grades[1]),sum(grades[2]),sum(grades[3]),sum(grades[4])
#print(sum_grades)

grades_index = len(grades[0]), len(grades[1]), len(grades[2]), len(grades[3]), len(grades[4])
#print(grades_index)

midlle_ball = sum_grades[0]/len(grades[0]), sum_grades[1]/len(grades[1]), sum_grades[2]/len(grades[2]), sum_grades[3]/len(grades[3]), sum_grades[4]/len(grades[4])
#print(midlle_ball)


midlle_ball_students = { students[0]:midlle_ball[0], students[1]:midlle_ball[1], students[2]:midlle_ball[2], students[3]:midlle_ball[3],students[4]:midlle_ball[4]}
print(midlle_ball_students)


