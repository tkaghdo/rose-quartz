import falcon


class User(object):

    def __init__(self, storage_path):
        self.storage_path = storage_path

    def on_get(self, req, resp, name):
        resp.body = '{"user":' + '\'' + name +'\'}'
        resp.status = falcon.HTTP_200
