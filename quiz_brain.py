class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False)?: ").lower()
        self.check_answer(user_answer=user_answer,
                          correct_answer=current_question.answer)

    def still_have_question(self):
        """return false if the question at current question is the last question"""
        if self.question_number == len(self.question_list):
            print("You've completed the quiz.")
            print(f"Your final score is {self.score}/{self.question_number}.")
            return False
        return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print(
                f"You got it right! Current score: {self.score}/{self.question_number}.")
        else:
            print(
                f"That's wrong. current score: {self.score}/{self.question_number}.")
        print(f"The correct answer is {correct_answer}.")
        print("\n")
