grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sum_grades1_ = sum(grades[0])
sum_grades2_ = sum(grades[1])
sum_grades3_ = sum(grades[2])
sum_grades4_ = sum(grades[3])
sum_grades5_ = sum(grades[4])
#print(sum_grades1_,sum_grades2_,sum_grades3_,sum_grades4_,sum_grades5_)

midlle1_ = sum_grades1_/5
midlle2_ = sum_grades2_/4
midlle3_ = sum_grades3_/4
midlle4_ = sum_grades4_/3
midlle5_ = sum_grades5_/5
#print(midlle1_,midlle2_,midlle3_,midlle4_,midlle5_)

#students = {'Johnny':[4, 5, 5, 2], 'Bilbo':[2, 2, 2, 3], 'Steve':[5, 5, 5, 4, 5], 'Khendrik':[4, 4, 3],'Aaron':[5, 3, 3, 5, 4]}
students = list
#print(students,type(students))
students = [['Johnny'], ['Bilbo'], ['Steve'], ['Khendrik'], ['Aaron']]
#print(students)

midlle_bul_students = {'Johnny':[midlle3_], 'Bilbo':[midlle2_], 'Steve':[midlle5_], 'Khendrik':[midlle4_],'Aaron':[midlle1_]}
print(midlle_bul_students)


