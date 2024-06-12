from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    new_q = Question(q_text, q_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
quiz.next_question()
while quiz.still_have_question():
    user_input = input(
        "Type 'exit' at any time to quit the quiz. Press Enter to continue...")
    if user_input.lower() == "exit":
        print("Exiting the quiz. Goodbye!")
        break
    quiz.next_question()
