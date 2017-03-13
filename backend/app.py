import falcon
import questions
import users
import signup

api = application = falcon.API()

#questions = questions.Question()
#api.add_route('/questions', questions)

# Sign up
sign_up = signup.SignUp()
api.add_route('/signup', sign_up)
api.add_route('/signup/{name}', sign_up)

# Users
# users = users.User()
# api.add_route('/users', users)
# api.add_route('/users/{name}', users)
