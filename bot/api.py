from django.conf import settings
import requests

api = {
    'login': {
        'url': 'api/auth/login/'
    },
    'schedule': {
        'url': 'api/days/{date}/',
        'params': ['date']
    }
}

class API:
    '''
    Utiltity for calling APIs

    usage: API(token).post(data)

    # login:
    API('login').post({username: '', password: ''})

    API('create.appointment', token).post(data)
    API('create.client', token).post(data)
    '''

    def __init__(self, resource, token=None):
        self.resource = resource
        self.token = token

    def get_url(self, params = None):
        path = api.get(self.resource).get('url')
        url = "{}/{}" . format(
            settings.APPOINTMENTGURU_API,
            path)
        if params:
            url = url . format(**params)

        return url

    def get_headers(self, extra_headers={}):
        headers = {}
        if self.token is not None:
            # headers['Authorization'] = 'Token {}' . format(self.token)
            headers['Authorization'] = 'Token 94e0dfaf48eb61ae9087fc22ab1afc3979822391'
        headers.update(extra_headers)
        return headers

    def get(self, params=None, extra_headers={}):
        url = self.get_url(params)
        return requests.get(
                url,
                headers=self.get_headers(extra_headers))

    def post(self, data, extra_headers={}):
        url = self.get_url()
        return requests.post(
                url,
                data,
                headers=self.get_headers(extra_headers))
