from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["question"],question["correct_answer"]))


quiz = QuizzBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Ypu've completed the quis")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
