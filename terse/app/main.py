import tornado.ioloop
import tornado.web

from db import couch
from redirect import RedirectHandler
from url import UrlApiHandler


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    if 'urls' not in couch:
        couch.create('urls')

    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/api/url/', UrlApiHandler),
        (r'/api/url/(\w+)/', UrlApiHandler),
        (r'/(\w+)/', RedirectHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
