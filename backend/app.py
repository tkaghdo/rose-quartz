import falcon
import questions
import users
import signup
import login
import langauges

api = application = falcon.API()

#questions = questions.Question()
#api.add_route('/questions', questions)

# Sign up route
sign_up = signup.SignUp()
api.add_route('/signup', sign_up)

# Login route
login_route = login.Login()
api.add_route('/login', login_route)

# Langauges route
lang_route = langauges.Languages()
api.add_route('/languages', lang_route)

# Users
# users = users.User()
# api.add_route('/users', users)
# api.add_route('/users/{name}', users)
