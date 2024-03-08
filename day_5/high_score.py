# Input a list of student scores
student_scores = "78 65 89 86 55 91 64 89".split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Write your code below this row 👇

score = 0
for n in student_scores:
    if n > score:
        score = n

print(f"The highest score in the class is: {score}")
