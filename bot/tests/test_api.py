from django.test import TestCase, Client, override_settings
from bot.api import API
from django.conf import settings

@override_settings(APPOINTMENTGURU_API = 'http://api.com')
class ApiTestCase(TestCase):

    def test_get_url(self):
        url = API('login').get_url()
        expected_url = 'http://api.com/api/auth/login/'
        assert url == expected_url

    def test_get_url_with_params(self):
        url = API('schedule').get_url(params={'date': '2016-12-01'})
        expected_url = 'http://api.com/api/days/2016-12-01/'
        assert url == expected_url

    def test_get_header_sets_auth_token(self):
        headers = API('login', '123').get_headers()

        assert headers.get('Authorization', 'Token 123')

    def test_can_set_extra_headers(self):

        headers = API('login').get_headers({'foo': 'bar'})

        assert headers.get('foo', 'bar')