import falcon
import questions

api = application = falcon.API()

questions = questions.Question()
api.add_route('/questions', questions)
