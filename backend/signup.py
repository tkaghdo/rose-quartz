import falcon
import mimetypes
import uuid
import json
import codecs
from utils.utils import Utilities
from model.db_ops import Data_Ops

class SignUp(object):

    def __init__(self):
        pass

    def insert_user(self, user):
        print(user)

    def on_get(self, req, resp, name):
        resp.body = '{"s":' + '\'' + name +'\'}'
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):

        # Example of post reqeust: http POST localhost:8000/signup Content-Type:application/json < signup_20170310.json
        # example of the body
        '''
        {
          "name":     "tamby",
          "email":    "tamby.kaghdo@gmail.com",
          "password": "myPassword"
        }
        '''

        # Content-Type
        ext = mimetypes.guess_extension(req.content_type)

        #json file
        filename = '{uuid}{ext}'.format(uuid=uuid.uuid4(), ext=ext)

        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body',
                                        'A valid JSON document is required.')
        try:
            sign_up_obj = json.loads(body.decode('utf-8'))

        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(falcon.HTTP_753,
                                   'Malformed JSON',
                                   'Could not decode the request body. The '
                                   'JSON was incorrect or not encoded as '
                                   'UTF-8.')

        # validate body
        u = Utilities()
        body_status, name_status, email_status, password_status = \
         u.validate_body(sign_up_obj, "SIGN_UP")

        # TODO insert user to database
        if body_status:
            insert_obj = Data_Ops()
            insert_obj.insert_user(sign_up_obj)
            resp.status = falcon.HTTP_201
        else:
            # TODO generate a log
            resp.status = falcon.HTTP_417
