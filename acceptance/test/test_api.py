from unittest import TestCase

import requests


class TestUrl(TestCase):
    def test_creates_and_can_use_redirect_url(self):
        response = requests.post('http://terse:8888/api/url/', json={
            'target': 'http://www.google.com/'
        })
        self.assertEqual(response.status_code, 201)

        redirect_id = response.json()['redirect_id']

        redirect_response = requests.get('http://terse:8888/%s/' % redirect_id)
        self.assertEqual(redirect_response.status_code, 200)
        self.assertEqual(redirect_response.history[0].status_code, 302)
