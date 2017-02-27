import sys
import json
import test.test

class User():

    def __init__(self, user_dict):
        self.user_name = user_dict["name"]
        self.email = user_dict["email"]
        self.level = 0


    def get_user_name(self):
        return self.user_name

    def get_email(self):
        return self.email

    def get_level(self):
        return self.level

def is_user_exists(user, database="file"):
    if database == "file":
        try:
            with open('../data/users.json') as data_file:
                data = json.load(data_file)
                for key in data:
                    print(key)
        except FileNotFoundError as e:
            print(e)
            sys.exit(e.errno)

def main():

    # SIMULATE CREATING A NEW USER

    # rq dict will come from the front end
    user_dict = {
        "name": "poop",
        "email": "poop@gmail.com",
    }

    r = User(user_dict)

    t = test.test.test()

    # place this new user in the "database"
    # --> check if the user is already in the database, provide a message if so
    #is_user_exists(u1)

    # --> if no user exists then create a record of the user


    # TODO: SIMULATE A NEW QUESTION QUEST


    # TODO: SIMULATE A CONTINUING QUEST


main()