class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        current_answer = self.question_list[self.question_number].answer.lower()
        self.question_number += 1
        response = input(f"Q.{self.question_number}. {current_question} (True/False)? ").lower()

        self.check_answer(response, current_answer)

    def still_has_questions(self):
        if self.question_number <= len(self.question_list) - 1:
            return True
        else:
            return False

    def check_answer(self, user_answer, current_answer):
        if user_answer == current_answer:
            print("You got it right!")
            self.score += 1

        # print(self.score)
        else:
            print("The correct answer is "+current_answer)
        print(f"Your current score is {self.score}/{self.question_number}")
        print("")
