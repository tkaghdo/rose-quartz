import falcon
import mimetypes
import uuid
import json
import codecs
import logging
from utils.utils import Utilities
from model.db_ops import Data_Ops


class SignUp(object):

    def __init__(self):
        # setup logging
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        fh = logging.FileHandler('logs/sign_up.log')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.setLevel(logging.INFO)


    def on_get(self, req, resp, name):
        resp.body = '{"name": "tamby"}'
        resp.status = falcon.HTTP_200
    '''
    def on_post(self, req, resp, name):
        resp.body = '{"name": "post"}'
        resp.status = falcon.HTTP_200
    '''

    def on_post(self, req, resp):

          # self.logger.info('info')
          # self.logger.error('error')

          # Example of post reqeust: http POST localhost:8000/signup Content-Type:application/json < signup_20170310.json
          # example of the body
          '''
          {
            "name":     "tamby",
            "email":    "tamby.kaghdo@gmail.com",
            "password": "myPassword"
          }
          '''
          body = req.stream.read()
          if not body:
              raise falcon.HTTPBadRequest('Empty request body',
                                          'A valid JSON document is required.')
              self.logger.error('Empty request body')
          try:
              sign_up_obj = json.loads(body.decode('utf-8'))

          except (ValueError, UnicodeDecodeError):
              raise falcon.HTTPError(falcon.HTTP_753,
                                     'Malformed JSON',
                                     'Could not decode the request body. The '
                                     'JSON was incorrect or not encoded as '
                                     'UTF-8.')
              self.logger.error('Malformed JSON')

          # validate body
          u = Utilities()
          body_status, name_status, email_status, password_status = \
           u.validate_body(sign_up_obj, "SIGN_UP")

          if body_status:
              insert_obj = Data_Ops()
              insert_status = insert_obj.insert_user(sign_up_obj)
              if insert_status:
                  resp.body = 'user signed up'
                  resp.status = falcon.HTTP_201
              else:
                  self.logger.error('Failed to create user record ' + str(sign_up_obj))
                  resp.status = falcon.HTTP_417
          else:
              self.logger.error('Failed to validate json object ' + str(sign_up_obj))
              resp.status = falcon.HTTP_417
