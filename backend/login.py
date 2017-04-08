import logging
from model.db_ops import Data_Ops

class Login(object):

    def __init__(self):
        # setup logging
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        fh = logging.FileHandler('logs/login.log')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.setLevel(logging.INFO)


    def on_post(self, req, resp):

        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body',
                                        'A valid JSON document is required.')
            self.logger.error('Empty request body')
        try:
            login_obj = json.loads(body.decode('utf-8'))

        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(falcon.HTTP_753,
                                   'Malformed JSON',
                                   'Could not decode the request body. The '
                                   'JSON was incorrect or not encoded as '
                                   'UTF-8.')
            self.logger.error('Malformed JSON')

        print("LOGIN OBJECT: ", login_obj)

        l_user = Data_Ops()
        status = l_user.login_user(login_obj)
        if status:
            # login succes
            resp.body = 'user logged in'
            resp.status = falcon.HTTP_201
        else:
            # login Fail
            self.logger.error('Faild to login user: ' + str(login_obj))
            resp.status = falcon.HTTP_417
