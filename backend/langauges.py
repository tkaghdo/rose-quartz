import falcon
import json
import logging
from model.db_ops import Data_Ops

class Languages(object):

    def __init__(self):
        # setup logging
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        fh = logging.FileHandler('logs/login.log')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.setLevel(logging.INFO)


    def on_get(self, req, resp):
        langs = Data_Ops()
        langs_list = langs.get_languages()
        if len(langs_list) == 0:
            resp.status = falcon.HTTP_204
        else:
            resp.body = json.dumps(langs_list)
            resp.status = falcon.HTTP_200
