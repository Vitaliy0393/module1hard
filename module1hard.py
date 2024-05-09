grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sum_grades = sum(grades[0]),sum(grades[1]),sum(grades[2]),sum(grades[3]),sum(grades[4])
#print(sum_grades)
midlle_ball = sum_grades[0]/5, sum_grades[1]/4, sum_grades[2]/4, sum_grades[3]/3, sum_grades[4]/5
#print(midlle_ball)


#students = {'Johnny':[4, 5, 5, 2], 'Bilbo':[2, 2, 2, 3], 'Steve':[5, 5, 5, 4, 5], 'Khendrik':[4, 4, 3],'Aaron':[5, 3, 3, 5, 4]}
students = list
#print(students,type(students))
students = [['Johnny'], ['Bilbo'], ['Steve'], ['Khendrik'], ['Aaron']]
#print(students)

midlle_ball_students = {'Johnny':midlle_ball[0], 'Bilbo':midlle_ball[1], 'Steve':midlle_ball[4], 'Khendrik':midlle_ball[3],'Aaron':midlle_ball[2]}
print(midlle_ball_students)


