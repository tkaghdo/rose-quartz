import datetime
import json
import sys

class Question_Session():

    def __init__(self, user, ctime):
        self.user = user
        self.question_posted_date_time = ctime
        try:
            with open('questions_answers.json') as data_file:
                self.data = json.load(data_file)
        except FileNotFoundError as e:
            print(e)
            sys.exit(e.errno)


    def question(self, question):
        # is this a valid question
        valid = False
        for key in self.data:
            if question.upper() == key:
                valid = True
        return valid

    def get_answer(self, question):
        self.answer = "AL RAJJUL"
        return



# start a session
q = Question_Session("tkaghdo", datetime.datetime.now())

# --> what is the rq level

# ask a rq a question

# --> get a question based on his level and he didn't answer yet
question_1 = "WHAT IS THE MAN"
print(q.question(question_1))



#print(get_answer(q.question("WHAT IS 'THE MAN'")))

