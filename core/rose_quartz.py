import sys
import json
from user.user import User



def is_user_exists(user, database="file"):
    email = user.get_email()
    user_exists = False
    user_id = None
    if database == "file":
        try:
            with open('../data/users.json') as data_file:
                data = json.load(data_file)
                for key in data:
                    user_list = data[key]
                    for user_dict in user_list:
                        if user_dict["email"] == email:
                            user_exists = True
                            user_id = user_dict["id"]
                            break

        except FileNotFoundError as e:
            print(e)
            sys.exit(e.errno)
    return user_exists, user_id

def main():

    # SIMULATE CREATING A NEW USER

    # rq dict will come from the front end
    user_dict = {
        "name": "poop",
        "email": "aa@gmail.com",
    }

    # create user object
    u2 = User(user_dict)

    # place this new user in the "database"
    # --> check if the user is already in the database, provide a message if so
    print(is_user_exists(u2))

    # --> if no user exists then create a record of the user


    # TODO: SIMULATE A NEW QUESTION QUEST


    # TODO: SIMULATE A CONTINUING QUEST


main()