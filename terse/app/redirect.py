import tornado

from db import couch


class RedirectHandler(tornado.web.RequestHandler):
    def get(self, redirect_id):
        doc = couch['urls'].get(redirect_id)
        self.redirect(doc['target'], status=302)
