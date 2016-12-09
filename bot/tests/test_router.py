from django.test import TestCase, Client
from django.core.urlresolvers import reverse

class RouterTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def test_routes(self):
        payload = {
            "result": {
                "action": "debug"
            }
        }
        result = self.client.post(
            self.url,
            payload,
            content_type='text/json')

        print (result.content)
