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

    def on_post(self, req, resp, name):
        resp.body = '{"name": "post"}'
        resp.status = falcon.HTTP_200
