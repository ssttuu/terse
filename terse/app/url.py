import json
import random
import string

import tornado

from db import couch


class UrlApiHandler(tornado.web.RequestHandler):
    URL_CHARACTERS = string.ascii_letters
    URL_LENGTH = 10

    def get_unique_id(self):
        unique_id = ''.join([random.choice(self.URL_CHARACTERS) for _ in range(self.URL_LENGTH)])

        if couch['urls'].get(unique_id):
            return self.get_unique_id()

        return unique_id

    def get_request_body(self):
        return json.loads(self.request.body.decode('utf-8'))

    def get(self, redirect_id=None):
        if not redirect_id:
            return self.write(json.dumps(couch['urls'].view('_all_docs')))

        doc = couch['urls'].get(redirect_id)
        return self.write(json.dumps(doc))

    def post(self):
        redirect_id = self.get_unique_id()

        request_data = self.get_request_body()

        if 'target' not in request_data:
            return self.send_error(400)

        doc = {
            '_id': redirect_id,
            'redirect_id': redirect_id,
            'target': request_data['target'],
        }

        _id, _rev = couch['urls'].save(doc)

        doc['_rev'] = _rev

        self.set_status(201)
        return self.write(json.dumps(doc))

    def patch(self, redirect_id=None):
        request_data = self.get_request_body()

        doc = couch['urls'].get(redirect_id)
        doc.update(request_data)

        couch['urls'].update(doc)

        return self.write(json.dumps(doc))
