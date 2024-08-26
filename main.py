grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student_set = list(students)
student_set.sort()

count = 0
pair_list = {student_set[count] : 0}
for grade in grades:
    average = sum(grade) / len(grade)
    name = student_set[count]
    pair_list.update({name: average})
    count += 1

print(pair_list)