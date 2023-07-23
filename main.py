from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for items in question_data:
    text_question = items['question']
    text_answer = items['correct_answer']
    question_obj = Question(text_question, text_answer)
    question_bank.append(question_obj)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
