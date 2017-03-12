import falcon


class User(object):

    def __init__(self):
        pass

    def on_get(self, req, resp, name):
        resp.body = '{"user":' + '\'' + name +'\'}'
        resp.status = falcon.HTTP_200
