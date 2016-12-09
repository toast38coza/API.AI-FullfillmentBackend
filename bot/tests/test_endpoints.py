from django.test import TestCase, Client
from django.core.urlresolvers import reverse

# todo: mocking etc. + responses

class EndpointTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def test_debug(self):

        payload = {
            "result": {
                "action": "debug",
                "parameters": {
                    "foo": "bar"
                }
            }
        }
        result = self.client.post(
            self.url,
            payload,
            content_type='text/json')

        token = result.json().get('fulfillment').get('data').get('token')
        assert token is not None
