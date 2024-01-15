from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def create_question_bank():
    question_bank = []

    for data in question_data:
        new_question = Question(q_text=data["text"], q_answer=data['answer'])
        question_bank.append(new_question)

    return question_bank


question_bank = create_question_bank()
quiz_brain = QuizBrain(question_list=question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()

print("You completed the quiz!")
print(f"Your final score {quiz_brain.score}/{quiz_brain.question_number}")