student_heights = ("156 178 165 171 187").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_heights = 0
number_of_students = 0
for height in student_heights:
    total_heights += height
    number_of_students += 1

average_height = round(total_heights / number_of_students)


print(
    f"total height = {total_heights}\nnumber of students"
    f" = {number_of_students}\naverage height = {average_height}"
)
