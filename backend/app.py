import falcon
import questions
import users

api = application = falcon.API()

questions = questions.Question()
api.add_route('/questions', questions)

users_storage_path = '/usr/local/var/look'

users = users.User(users_storage_path)
api.add_route('/users', users)

api.add_route('/users/{name}', users)
