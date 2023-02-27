from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=QuestionModel(question_text,question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_question():
    QuizBrain.next_question(quiz)

print("Your quiz is completed!")
print(f"Your score is {quiz.score}/{quiz.question_number}")