class Utilities():

    def __init__(self):
        pass

    def validate_name(self, name):
        valid = True
        if name == None or name == '' or len(name) == 0:
            valid = False

        return valid

    def validate_email(self, email):

        # TODO need better checks
        valid = True
        if email == None or email == '' or len(email) == 0:
            valid = False

        return valid

    def validate_password(self, password):
        # TODO need better checks
        valid = True
        if password == None or password == '' or len(password) < 8:
            valid = False

        return valid


    def validate_body(self, body, which_body):
        valid = True
        # validate sign up data
        if which_body == 'SIGN_UP':
            # is valid name
            name_status = self.validate_name(body['name'])
            email_status = self.validate_email(body['email'])
            password_status = self.validate_password(body['password'])
            if not (email_status and email_status and password_status):
                valid = False

        return valid, name_status, email_status, password_status
