from data import trivia_json_data
from tkinter import Tk
from tkinter import *

trivia_ques_list = []

# TODO Create a list of dictionaries with question and answer pair
for elem_dict in trivia_json_data:
    # TODO Format the data and add it to the dictionary
    trivia_ques_dict = {'question': elem_dict['question'], 'answer': elem_dict['correct_answer']}

    # TODO Append the dicts to a list
    trivia_ques_list.append(trivia_ques_dict)

# TODO Ask the questions
question_no = 0
correct_answers = 0

ask_question = True
while ask_question:
    if question_no >= len(trivia_ques_list):
        ask_question = False
    else:
        question_no += 1
        question_index = question_no-1

        question = trivia_ques_list[question_index]['question']
        # TODO Add the quotes in the string question
        question = question.replace("&quot;", "'")
        question = question.replace("&#039;", "'")

        answer = trivia_ques_list[question_index]['answer']

        # TODO Ask a question
        response_answer = input(f"Q{question_no}. {question} True or False?: ").lower()


        # TODO Loop until the correct answer is given
        invalid_response = True
        while invalid_response:
            if response_answer != "true" and response_answer != "false":
                print("Answer with either 'True' or 'False'.")
                response_answer = input(f"Q{question_no}. {question} True or False?: ").lower()
            else:
                invalid_response = False

        # TODO Check whether the answer is correct
        if response_answer == answer.lower():
            print("Correct!")
            # TODO Add to the score
            correct_answers += 1
        else:
            print("Wrong")

    print("")

print(f"You've answered {correct_answers} questions correctly. Congrats")


