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