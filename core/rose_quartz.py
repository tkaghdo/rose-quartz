import sys
import json
from user.user import User
import logging

def add_user(user, new_user_id, database="file"):
    user_dict = {"id": new_user_id, "name": user.user_name, "email": user.email, "level": user.level}
    if database == "file":
        try:
            with open('../data/users.json') as data_file:
                data = json.load(data_file)
                data.append(user_dict)

            with open('../data/users.json', 'w') as data_file:
                json.dump(data, data_file)


        except FileNotFoundError as e:
            print(e)
            sys.exit(e.errno)


def get_max_user_id(database="file"):
    if database == "file":
        try:
            with open('../data/users.json') as data_file:
                data = json.load(data_file)
                max_id = 0
                for user in data:
                    if user["id"] > max_id:
                        max_id = user["id"]

        except FileNotFoundError as e:
            print(e)
            sys.exit(e.errno)

    return max_id


def is_user_exists(user, database="file"):
    """
    looks if a user exists or not in the database
    :param user: a user object
    :param database: the database where the users live. By default its a JSON file
    :return: a boolean if the user exists or not and the id of the user if exists
    """
    email = user.email
    user_exists = False
    user_id = None
    if database == "file":
        try:
            with open('../data/users.json') as data_file:
                data = json.load(data_file)
                for user in data:
                    if user["email"] == email:
                        user_exists = True
                        user_id = user["id"]
                        break

        except FileNotFoundError as e:
            print(e)
            sys.exit(e.errno)

    return user_exists, user_id


def main():
    logging.basicConfig(filename="../logs/sample.log", level=logging.INFO)
    log = logging.getLogger(__name__)
    log.info("Informational message")
    log.error("An error has happened!")

    # SIMULATE CREATING A NEW USER

    # rq dict will come from the front end
    user_dict = {
        "name": "poop",
        "email": "zz@gmail.com",
    }

    # create user object
    u2 = User(user_dict)

    # place this new user in the "database"
    # check if the user is already in the database, provide a message if so
    user_status, user_id = is_user_exists(u2)

    if user_status == True:
        print("User {0} already exists".format( u2.get_email()))
        sys.exit(1)
    else:
        # add user to database
        new_user_id = None
        if get_max_user_id() == None:
            new_user_id = 1
        else:
            new_user_id = get_max_user_id() + 1
            add_user(u2,new_user_id)
            print("User {0} added".format(u2.email))


    # --> if no user exists then create a record of the user


    # TODO: SIMULATE A NEW QUESTION QUEST


    # TODO: SIMULATE A CONTINUING QUEST


main()