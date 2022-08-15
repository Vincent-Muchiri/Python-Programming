from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for elem in range(0, len(question_data)):
    question_text = question_data[elem]["text"]
    question_answer = question_data[elem]["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[0].text)

new_quizbrain = QuizBrain(question_bank)
while new_quizbrain.still_has_questions():
    # print(question_bank)
    new_quizbrain.next_question()

print("")
print(f"Your final score is {new_quizbrain.score}/{new_quizbrain.question_number}")